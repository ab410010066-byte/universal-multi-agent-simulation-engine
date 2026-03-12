from __future__ import annotations

import json
from dataclasses import asdict
from pathlib import Path
from typing import Iterable

from .types import WorldEvent


class JsonlEventLogger:
    def __init__(self, output_dir: str) -> None:
        self.output_path = Path(output_dir)
        self.output_path.mkdir(parents=True, exist_ok=True)

    def write_events(self, events: Iterable[WorldEvent]) -> Path:
        path = self.output_path / "events.jsonl"
        with path.open("w", encoding="utf-8") as handle:
            for event in events:
                payload = {
                    **asdict(event),
                    "timestamp": event.timestamp.isoformat(),
                }
                handle.write(json.dumps(payload) + "\n")
        return path

    def write_summary(self, summary: dict) -> Path:
        path = self.output_path / "summary.json"
        with path.open("w", encoding="utf-8") as handle:
            json.dump(summary, handle, indent=2)
        return path
