from __future__ import annotations

from collections import deque, defaultdict
from dataclasses import asdict
from typing import Deque, Dict, List

from .types import WorldEvent


class MemoryManager:
    def __init__(self, window_size: int = 5) -> None:
        self.window_size = window_size
        self._store: Dict[str, Deque[WorldEvent]] = defaultdict(lambda: deque(maxlen=self.window_size))

    def record(self, agent_id: str, event: WorldEvent) -> None:
        self._store[agent_id].append(event)

    def recent(self, agent_id: str) -> List[dict]:
        return [
            {
                "step": event.step,
                "timestamp": event.timestamp.isoformat(),
                "source": event.source,
                "event_type": event.event_type,
                "payload": event.payload,
                "routed_layer": event.routed_layer,
            }
            for event in self._store.get(agent_id, [])
        ]
