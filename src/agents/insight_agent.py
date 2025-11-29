import json, os
from pathlib import Path
from src.utils.llm_client import call_llm

PROMPT_PATH = "prompts/insight_prompt.md"

class InsightAgent:
    def generate(self, df, plan):
        # compute overall summary and top segments
        overall = {
            "total_spend": float(df["spend"].sum()),
            "total_revenue": float(df["revenue"].sum()) if "revenue" in df else None,
            "overall_roas": float(df["roas"].mean())
        }
        # compute campaign-level roas and ctr
        campaigns = df.groupby("campaign_name").agg({
            "spend":"sum","revenue":"sum","impressions":"sum","clicks":"sum","roas":"mean","ctr":"mean"
        }).reset_index().sort_values("roas", ascending=False).head(plan.get("top_k_segments",5))
        payload = {
            "plan": plan,
            "overall": overall,
            "campaigns_topk": campaigns.head(5).to_dict(orient="records")
        }
        prompt = Path(PROMPT_PATH).read_text()
        system = prompt.split("TASK:")[0]
        user_content = json.dumps(payload, indent=2)
        # call LLM
        llm_response = call_llm(system, user_content, temp=0.2, max_tokens=700)
        try:
            parsed = json.loads(llm_response)
        except Exception:
            parsed = {"id":"overall_performance","narrative": llm_response, "confidence": 0.5}
        result = {"overall": overall, "insights": [parsed]}
        return result
