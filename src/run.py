#!/usr/bin/env python3
import argparse, json, os, time
from src.orchestrator import Orchestrator

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("instruction", help="High-level instruction, e.g. 'Analyze ROAS drop in last 7 days'")
    args = parser.parse_args()

    orchestrator = Orchestrator()
    outputs = orchestrator.run(args.instruction)

    ts = int(time.time())
    os.makedirs("reports", exist_ok=True)
    with open(f"reports/insights_{ts}.json", "w", encoding="utf-8") as f:
        json.dump(outputs["insights"], f, indent=2, ensure_ascii=False)
    with open(f"reports/creatives_{ts}.json", "w", encoding="utf-8") as f:
        json.dump(outputs["creatives"], f, indent=2, ensure_ascii=False)
    with open(f"reports/report_{ts}.md", "w", encoding="utf-8") as f:
        f.write(outputs["report_md"])

    print("Generated reports in reports/")

if __name__ == "__main__":
    main()
