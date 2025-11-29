import os, json, time
from src.agents.planner import PlannerAgent
from src.agents.data_agent import DataAgent
from src.agents.insight_agent import InsightAgent
from src.agents.evaluator import EvaluatorAgent
from src.agents.creative_generator import CreativeGenerator
from src.reporter import Reporter
from pathlib import Path

class Orchestrator:
    def __init__(self, config_path="config/config.yaml"):
        self.planner = PlannerAgent()
        self.data_agent = DataAgent()
        self.insight_agent = InsightAgent()
        self.evaluator = EvaluatorAgent()
        self.creative_generator = CreativeGenerator()
        self.reporter = Reporter()

    def run(self, instruction: str):
        plan = self.planner.plan(instruction)
        df = self.data_agent.load_and_prepare(plan)
        insight_payload = self.insight_agent.generate(df, plan)
        evaluated = self.evaluator.validate(df, insight_payload)
        creatives = self.creative_generator.generate(df, evaluated)
        report_md = self.reporter.build(evaluated, creatives)
        outputs = {"insights": evaluated, "creatives": creatives, "report_md": report_md}
        # logs
        os.makedirs("logs", exist_ok=True)
        ts = int(time.time())
        Path(f"logs/run_{ts}.json").write_text(json.dumps(outputs, indent=2, ensure_ascii=False))
        return outputs
