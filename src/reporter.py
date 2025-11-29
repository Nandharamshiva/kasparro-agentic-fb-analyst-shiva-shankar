class Reporter:
    def build(self, evaluated: dict, creatives: dict) -> str:
        out = []
        out.append("# Facebook Ads Performance Report\n")
        out.append("## Executive summary\n")
        overall = evaluated.get("overall", {})
        out.append(f"- Total Spend: {overall.get('total_spend', 0):.2f}")
        if "total_revenue" in overall:
            out.append(f"- Total Revenue: {overall.get('total_revenue', 0):.2f}")
            out.append(f"- Overall ROAS: {overall.get('overall_roas', 0):.2f}x")
        out.append("\n## Key insights\n")

        # iterate through insights
        for ins in evaluated.get("insights", []):
            out.append(f"### {ins.get('id', 'insight')}")
            out.append("")
            if "insights" in ins:
                for bullet in ins["insights"]:
                    out.append(f"- {bullet}")
            out.append("")
            if "actions" in ins:
                out.append("**Actions:**")
                for act in ins["actions"]:
                    out.append(f"- {act}")
            out.append("")

        out.append("## Creative Recommendations\n")
        for c in creatives.get("creatives", []):
            out.append(f"### {c.get('id')} — {c.get('angle')}")
            out.append(f"- Target Segment: {c.get('target_segment')}")
            out.append(f"- Primary Text: {c.get('primary_text')}")
            out.append(f"- Headline: {c.get('headline')}")
            out.append(f"- CTA: {c.get('call_to_action')}")
            out.append(f"- Format: {c.get('format')}")
            out.append("")

        return "\n".join(out)
