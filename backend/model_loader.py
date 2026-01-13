import pickle
import os

MODEL_PATH = "artifacts/gb_pipeline.pkl"

if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError("Model artifact not found. Run train.py first.")

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

# Load feature ranges for input monitoring
FEATURE_RANGES_PATH = "artifacts/feature_ranges.pkl"
if not os.path.exists(FEATURE_RANGES_PATH):
    raise FileNotFoundError("Feature ranges not found. Run train.py first.")

with open(FEATURE_RANGES_PATH, "rb") as f:
    FEATURE_RANGES = pickle.load(f)
