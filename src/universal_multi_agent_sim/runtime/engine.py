from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, Iterable, List

from ..adapters.base import AgentAdapter
from .routing import RoutingPolicy


@dataclass
class SimulationEngine:
    """Minimal runtime skeleton for layered simulation experiments."""

    routing_policy: RoutingPolicy
    event_log: List[Dict[str, Any]] = field(default_factory=list)

    def step(
        self,
        agents: Iterable[AgentAdapter],
        observation: Dict[str, Any],
        context: Dict[str, Any],
    ) -> List[Dict[str, Any]]:
        actions: List[Dict[str, Any]] = []
        for agent in agents:
            tier = self.routing_policy.select_tier(agent=agent, observation=observation, context=context)
            action = agent.act(observation=observation, context={**context, "selected_tier": tier})
            self.event_log.append({"agent": agent.__class__.__name__, "tier": tier, "action": action})
            actions.append(action)
        return actions
