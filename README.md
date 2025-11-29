### kasparro-agentic-fb-analyst-shiva-shankar

Agentic multi-agent system designed for the Kasparro AI Applied Analyst Assignment.
This project diagnoses ROAS changes, generates insights, evaluates statistical evidence, and produces new creative concepts for an undergarments brand using a structured LLM-first workflow.

## 1. Quick Start
Requirements

Python ≥ 3.10

pip (latest)

Virtual environment recommended

Setup
python -m venv .venv
.venv\Scripts\activate   # Windows
or
source .venv/bin/activate  # Mac/Linux

pip install -r requirements.txt

## 2. Run the System
python -m src.run "Analyze ROAS drop in last 14 days"


This generates:

reports/insights_<timestamp>.json

reports/creatives_<timestamp>.json

reports/report_<timestamp>.md

logs/run_<timestamp>.json

 ## 3. Data Input

Place your dataset at:

data/synthetic_fb_ads_undergarments.csv


The dataset is automatically loaded based on:

config/config.yaml


Set:

use_sample_data: false
data_csv: data/synthetic_fb_ads_undergarments.csv

 ## 4. Architecture Overview

This system follows a Planner → Data → Insight → Evaluator → Creative → Reporter pipeline.

Agents:

PlannerAgent: Breaks task into structured subtasks

DataAgent: Loads, cleans, computes metrics

InsightAgent: Uses LLM for hypotheses & insights

EvaluatorAgent: Runs statistical tests to validate insights

CreativeGenerator: Creates new creative concepts

Reporter: Produces final marketer-facing report

Prompts stored under prompts/ as required.

Agent flow described in agent_graph.md.

##  5. Repository Layout
src/
  agents/
  utils/
prompts/
config/
reports/
logs/
data/
tests/

##  6. Testing
pytest -q


Includes evaluator tests to ensure pipeline stability.

## 7. Observability

Each run writes logs to:

logs/run_<timestamp>.json


Can be extended with Langfuse or custom JSON logs.

##  8. GitHub Release (Required)

Create release:

v1.0


Attach commit hash & link in the Google Form.

## 9. Submission Checklist

Repo name:
kasparro-agentic-fb-analyst-shiva-shankar
1. README formatted using template
2. prompts stored in /prompts
3. agents modularized in /src/agents
4. insights.json, creatives.json, report.md in /reports
5. logs present
6. PR titled “self-review”
7. GitHub release tag v1.0
