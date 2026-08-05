from pydantic import BaseModel, Field, computed_field, field_validator
from typing import Dict

class predictionResponse(BaseModel):
    predicted_category: str = Field(..., description="The predicted category for the user input",example="High")
    confidence: float = Field(..., description="The confidence score of the prediction(range: 0-1)", example=0.8432)
    class_probabilities: Dict[str, float] = Field(..., description="A dictionary containing the probabilities for each class",
                                                  example={"low": 0.01, "medium": 0.15, "high": 0.84})

    