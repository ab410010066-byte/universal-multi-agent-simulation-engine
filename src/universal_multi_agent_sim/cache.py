from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, Optional


@dataclass
class SemanticCache:
    store: Dict[str, dict] = field(default_factory=dict)

    def get(self, key: str) -> Optional[dict]:
        return self.store.get(key)

    def put(self, key: str, value: dict) -> None:
        self.store[key] = value
