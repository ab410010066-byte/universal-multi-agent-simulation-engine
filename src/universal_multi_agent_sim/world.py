from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List

from .types import Action, Event


@dataclass
class WorldEngine:
    scenario_name: str
    state: Dict[str, float | int | str | dict] = field(default_factory=dict)
    events: List[Event] = field(default_factory=list)

    def apply_action(self, step: int, action: Action, timestamp: str, routed_layer: str) -> Event:
        sentiment_delta = float(action.details.get("sentiment_delta", 0.0))
        demand_delta = float(action.details.get("demand_delta", 0.0))
        policy_delta = float(action.details.get("policy_delta", 0.0))
        macro_delta = float(action.details.get("macro_delta", 0.0))

        self.state["sentiment_index"] = float(self.state.get("sentiment_index", 0.0)) + sentiment_delta
        self.state["demand_index"] = float(self.state.get("demand_index", 0.0)) + demand_delta
        self.state["policy_signal"] = float(self.state.get("policy_signal", 0.0)) + policy_delta
        self.state["macro_pressure"] = float(self.state.get("macro_pressure", 0.0)) + macro_delta
        self.state["last_actor"] = action.agent_id

        event = Event(
            step=step,
            source=action.agent_id,
            event_type=action.action_type,
            payload=action.details,
            timestamp=timestamp,
            importance=action.importance,
            routed_layer=routed_layer,
        )
        self.events.append(event)
        return event

    def snapshot(self) -> Dict[str, float | int | str | dict]:
        return dict(self.state)