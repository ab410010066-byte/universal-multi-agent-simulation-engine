import json
from pathlib import Path

from universal_multi_agent_sim.engine import run_from_config


def test_minimal_simulation_writes_expected_outputs(tmp_path):
    repo_root = Path(__file__).resolve().parents[1]
    source_config = repo_root / "configs" / "minimal.yaml"
    config_text = source_config.read_text(encoding="utf-8").replace("outputs/run_local", str(tmp_path / "run_local"))
    config_path = tmp_path / "minimal.yaml"
    config_path.write_text(config_text, encoding="utf-8")

    summary = run_from_config(str(config_path))

    assert summary["scenario_name"] == "minimal-local-run"
    summary_path = tmp_path / "run_local" / "summary.json"
    events_path = tmp_path / "run_local" / "events.jsonl"
    assert summary_path.exists()
    assert events_path.exists()
    stored = json.loads(summary_path.read_text(encoding="utf-8"))
    assert stored["event_count"] == 16
    assert len(events_path.read_text(encoding="utf-8").strip().splitlines()) == 16
