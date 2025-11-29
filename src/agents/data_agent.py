import pandas as pd
import numpy as np
from pathlib import Path
import yaml

CONFIG_PATH = "config/config.yaml"

class DataAgent:
    def __init__(self, config_path=CONFIG_PATH):
        self.config = self._load_config(config_path)

    def _load_config(self, path):
        import yaml
        with open(path, "r") as f:
            return yaml.safe_load(f)

    def load_and_prepare(self, plan):
        path = self.config.get("data_csv")
        df = pd.read_csv(path, parse_dates=["date"])
        # normalize columns
        df.columns = [c.strip().lower() for c in df.columns]
        # basic metrics fallback
        if "ctr" not in df.columns and "clicks" in df.columns and "impressions" in df.columns:
            df["ctr"] = df["clicks"] / df["impressions"].replace(0, 1)
        if "roas" not in df.columns and "revenue" in df.columns and "spend" in df.columns:
            df["roas"] = df["revenue"] / df["spend"].replace(0, 1)
        # ensure numeric types
        for col in ["spend","impressions","clicks","purchases","revenue","roas","ctr"]:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)
        # add derived
        df["cpc"] = df.apply(lambda r: (r["spend"]/r["clicks"]) if r["clicks"]>0 else 0, axis=1)
        return df
