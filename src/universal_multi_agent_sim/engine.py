from __future__ import annotations

from pathlib import Path
from typing import Dict, List

import yaml

from .agents import (
    ArchetypeGroup,
    KeyIndividualAgent,
    MacroStatisticalPopulation,
    TemplatedAdaptiveAgent,
)
from .adapters.mock_adapter import MockAgentAdapter
from .cache import SemanticCache
from .logging_utils import JsonlEventLogger
from .memory import MemoryManager
from .router import ModelRouter
from .scheduler import EventScheduler
from .types import AgentContext, SimulationConfig
from .world import WorldEngine


class SimulationEngine:
    def __init__(self, config: SimulationConfig) -> None:
        self.config = config
        self.world = WorldEngine(config.scenario_name, dict(config.world))
        self.scheduler = EventScheduler(
            start_time=self._parse_start_time(config.scheduler.get("start_time", "2026-01-01T09:00:00")),
            step_minutes=int(config.scheduler.get("step_minutes", 5)),
        )
        self.router = ModelRouter(layer_thresholds={
            "key_individual": float(config.router.get("key_individual", 0.8)),
            "templated_adaptive": float(config.router.get("templated_adaptive", 0.5)),
            "archetype_group": float(config.router.get("archetype_group", 0.25)),
        }, budget=config.budget)
        self.memory = MemoryManager(window_size=int(config.world.get("memory_window", 5)))
        self.cache = SemanticCache()
        self.logger = JsonlEventLogger(config.output_dir)
        self.agents = self._build_agents(config.agents, config.macro_population)
        for scheduled_event in config.scheduler.get("events", []):
            self.scheduler.schedule(int(scheduled_event["step"]), scheduled_event)

    @staticmethod
    def _parse_start_time(value: str):
        from datetime import datetime

        return datetime.fromisoformat(value)

    @classmethod
    def from_yaml(cls, path: str) -> "SimulationEngine":
        with open(path, "r", encoding="utf-8") as handle:
            raw = yaml.safe_load(handle)
        config = SimulationConfig(
            scenario_name=raw["scenario_name"],
            steps=int(raw.get("steps", 1)),
            output_dir=raw.get("output_dir", "outputs/run_local"),
            budget=float(raw.get("budget", 1.0)),
            seed=int(raw.get("seed", 0)),
            world=raw.get("world", {}),
            scheduler=raw.get("scheduler", {}),
            router=raw.get("router", {}),
            agents=raw.get("agents", []),
            macro_population=raw.get("macro_population", {}),
        )
        return cls(config)

    def _build_agents(self, agents_config: List[Dict], macro_population: Dict) -> List:
        result = []
        layer_map = {
            "Layer 1 Key Individual Agents": KeyIndividualAgent,
            "Layer 2 Templated Adaptive Agents": TemplatedAdaptiveAgent,
            "Layer 3 Archetype Groups": ArchetypeGroup,
            "Layer 4 Macro Statistical Population": MacroStatisticalPopulation,
        }
        combined = list(agents_config)
        if macro_population:
            combined.append(macro_population)
        for entry in combined:
            adapter = MockAgentAdapter(
                name=entry["agent_id"],
                base_importance=float(entry.get("importance", 0.4)),
                profile=entry.get("profile", {}),
            )
            cls = layer_map[entry["layer"]]
            result.append(
                cls(
                    agent_id=entry["agent_id"],
                    adapter=adapter,
                    cohort_size=int(entry.get("cohort_size", 1)),
                    metadata=entry.get("metadata", {}),
                )
            )
        return result

    def run(self) -> dict:
        for step in range(self.config.steps):
            timestamp = self.scheduler.timestamp_for_step(step)
            scheduled_events = self.scheduler.pop_step_events(step)
            pressure = sum(float(evt.get("pressure", 0.0)) for evt in scheduled_events)
            if scheduled_events:
                self.world.state["policy_signal"] = float(self.world.state.get("policy_signal", 0.0)) + sum(
                    float(evt.get("policy_delta", 0.0)) for evt in scheduled_events
                )
            for agent in self.agents:
                observation = {
                    "pressure": pressure,
                    "scheduled_events": scheduled_events,
                    "world_state": self.world.snapshot(),
                }
                context = AgentContext(
                    step=step,
                    scenario=self.config.scenario_name,
                    world_state=self.world.snapshot(),
                    recent_events=[{
                        "step": evt.step,
                        "source": evt.source,
                        "event_type": evt.event_type,
                    } for evt in self.world.events[-5:]],
                    budget_remaining=self.router.budget,
                )
                importance = agent.importance_score()
                event_criticality = max([float(evt.get("criticality", 0.0)) for evt in scheduled_events], default=0.0)
                routed_layer = self.router.route(importance, event_criticality, agent.cohort_size)
                cache_key = f"{agent.agent_id}:{step}:{round(pressure, 3)}:{round(self.world.state.get('policy_signal', 0.0), 3)}"
                action = self.cache.get(cache_key)
                if action is None:
                    action = agent.act(observation, context)
                    self.cache.put(cache_key, action)
                event = self.world.apply_action(step, action, timestamp, routed_layer)
                self.memory.record(agent.agent_id, event)
                agent.update_memory({
                    "step": event.step,
                    "event_type": event.event_type,
                    "payload": event.payload,
                })
                self.router.consume_budget(routed_layer)
        summary = {
            "scenario_name": self.config.scenario_name,
            "steps": self.config.steps,
            "event_count": len(self.world.events),
            "final_world_state": self.world.snapshot(),
            "budget_remaining": round(self.router.budget, 4),
            "agents": [agent.agent_id for agent in self.agents],
            "output_dir": self.config.output_dir,
        }
        self.logger.write_events(self.world.events)
        self.logger.write_summary(summary)
        return summary


def run_from_config(config_path: str) -> dict:
    engine = SimulationEngine.from_yaml(config_path)
    return engine.run()
