# Agent Graph & Roles

Planner Agent:
 - Input: user instruction (CLI)
 - Responsibilities: break task into subtasks (time ranges, segments, metrics to compute)
 - Output: plan JSON to orchestrator

Data Agent:
 - Loads CSV, cleans, computes base metrics (CTR, CPC, CPM, ROAS)
 - Produces summarized numeric payloads for Insight & Evaluator

Insight Agent:
 - Receives summaries, planner questions
 - Generates hypotheses in natural language (+ requested JSON schema) using LLM via prompt files

Evaluator Agent:
 - Receives hypotheses + raw data snapshots
 - Runs quantitative tests (t-tests, ratio comparisons, trend detection)
 - Returns evidence, p-values, and confidence

Creative Generator:
 - Receives low-CTR campaign details and sample creatives
 - Uses LLM to output structured creative concepts (creatives.json)

Orchestrator (run.py):
 - Calls Planner -> Data -> Insight -> Evaluator -> Creative -> Report -> Save logs

Observability:
 - All agents produce JSON logs saved to logs/ with timestamped filenames.
