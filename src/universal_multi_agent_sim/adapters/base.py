from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Dict


class AgentAdapter(ABC):
    """Minimal adapter contract for external agents."""

    @abstractmethod
    def act(self, observation: Dict[str, Any], context: Dict[str, Any]) -> Dict[str, Any]:
        raise NotImplementedError

    @abstractmethod
    def update_memory(self, event: Dict[str, Any]) -> None:
        raise NotImplementedError

    @abstractmethod
    def importance_score(self) -> float:
        raise NotImplementedError
