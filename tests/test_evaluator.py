import json, os
from src.orchestrator import Orchestrator
def test_run_creates_reports(tmp_path):
    orch = Orchestrator()
    outputs = orch.run("Analyze ROAS drop")
    assert "insights" in outputs
    assert "creatives" in outputs
    assert isinstance(outputs["insights"], dict)
