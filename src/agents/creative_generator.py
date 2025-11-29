import json
from pathlib import Path
from src.utils.llm_client import call_llm

PROMPT_PATH = "prompts/creative_prompt.md"

class CreativeGenerator:
    def generate(self, df, evaluated):
        # find low-ctr campaigns
        camp = df.groupby("campaign_name").agg({"ctr":"mean","impressions":"sum","clicks":"sum"}).reset_index()
        low = camp.sort_values("ctr").head(4).to_dict(orient="records")
        sample_creatives = df[["campaign_name","creative_message","creative_type"]].dropna().head(10).to_dict(orient="records")
        payload = {"low_ctr_campaigns": low, "sample_creatives": sample_creatives}
        prompt = Path(PROMPT_PATH).read_text()
        system = prompt.split("TASK:")[0]
        user_content = json.dumps(payload, indent=2)[:3800]
        llm_response = call_llm(system, user_content, temp=0.7, max_tokens=900)
        try:
            parsed = json.loads(llm_response)
        except Exception:
            parsed = {"creatives": [{"id":"c1","raw": llm_response}]}
        return parsed
