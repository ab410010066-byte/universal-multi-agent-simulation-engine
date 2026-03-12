from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict


@dataclass
class RoutingPolicy:
    """Simple importance-based routing placeholder."""

    high_fidelity_threshold: float = 0.8
    medium_fidelity_threshold: float = 0.4

    def select_tier(self, agent: Any, observation: Dict[str, Any], context: Dict[str, Any]) -> str:
        score = float(agent.importance_score())
        if score >= self.high_fidelity_threshold:
            return "layer_1_high_fidelity"
        if score >= self.medium_fidelity_threshold:
            return "layer_2_template"
        return "layer_3_or_4_compressed"
