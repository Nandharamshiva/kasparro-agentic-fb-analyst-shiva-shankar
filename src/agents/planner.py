class PlannerAgent:
    def plan(self, instruction: str):
        # simple decomposition for this assessment
        return {
            "instruction": instruction,
            "time_window": "last_14_days",
            "top_k_segments": 5,
            "focus_metric": "roas"
        }
