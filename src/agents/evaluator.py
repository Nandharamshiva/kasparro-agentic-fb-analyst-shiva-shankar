import numpy as np
import pandas as pd
from scipy import stats

class EvaluatorAgent:
    def validate(self, df: pd.DataFrame, insight_payload: dict):
        # sample validations: detect significant roas drop across time windows
        df = df.copy()
        df = df.sort_values("date")
        # define two windows
        cutoff = df["date"].max() - pd.Timedelta(days=14)
        recent = df[df["date"] > cutoff]
        prev = df[df["date"] <= cutoff]
        recent_roas = recent["roas"].mean() if len(recent)>0 else 0
        prev_roas = prev["roas"].mean() if len(prev)>0 else 0
        # p-value via t-test on per-day roas if possible
        try:
            daily_recent = recent.groupby("date")["roas"].mean()
            daily_prev = prev.groupby("date")["roas"].mean()
            if len(daily_recent)>1 and len(daily_prev)>1:
                t,p = stats.ttest_ind(daily_recent, daily_prev, equal_var=False, nan_policy="omit")
            else:
                t,p = 0,1.0
        except Exception:
            t,p = 0,1.0
        evidence = {
            "recent_roas": float(recent_roas),
            "prev_roas": float(prev_roas),
            "t_stat": float(t),
            "p_value": float(p),
            "drop_pct": float((prev_roas - recent_roas)/prev_roas) if prev_roas>0 else 0.0
        }
        # attach evidence to each insight
        for ins in insight_payload.get("insights", []):
            ins["evidence"] = evidence
            ins["confidence"] = 0.5 if p>0.05 else 0.8
        insight_payload["overall"] = {"total_spend": float(df["spend"].sum()), "total_impressions": int(df["impressions"].sum())}
        return insight_payload
