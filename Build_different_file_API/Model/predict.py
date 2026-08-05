from pathlib import Path
import pickle
import pandas as pd

MODEL_PATH = Path(__file__).parent / "model.pkl"

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

MODEL_VERSION = "1.0.0"


class_labels = model.classes_.tolist()  # Get the class labels from the model
def predict_output(user_input: dict):
    df = pd.DataFrame([user_input])
    predicted_class = model.predict(df)[0]
    probabilities = model.predict_proba(df)[0]
    confidence = max(probabilities)  # Get the maximum probability as confidence
    class_probs = dict(zip(class_labels,map(lambda p: round(p, 4), probabilities)))  # Create a dictionary of class probabilities

    return {
        "predicted_category": predicted_class,
        "confidence": confidence,
        "class_probabilities": class_probs
    }