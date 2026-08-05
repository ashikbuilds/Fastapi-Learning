from fastapi import FastAPI
from fastapi.responses import JSONResponse
from Schema.user_input import UserInput
from Model.predict import predict_output, MODEL_VERSION,model
from Schema.prediction_response import predictionResponse

app = FastAPI()


@app.get('/')
def home():
    return {
        'message': 'Welcome to the Insurance Premium Prediction API',
        'model_version': MODEL_VERSION,
        'endpoints': {
            '/predict': {
                'method': 'POST',
                'description': 'Predicts the insurance premium category based on user input',
                'input_format': {
                    'age': 'int (1-120)',
                    'weight': 'float (kg)',
                    'height': 'float (m)',
                    'income_lpa': 'float (lpa)',
                    'smoker': 'bool',
                    'city': 'str',
                    'occupation': "str (one of ['retired', 'freelancer', 'student', 'government_job', 'business_owner', 'unemployed', 'private_job'])"
                },
                'output_format': {
                    'predicted_category': "str ('low', 'medium', or 'high')"
                }
            }
        }
    }

@app.get('/health')
def health_check():
    return{
        'status': 'healthy',
        'model_version': MODEL_VERSION,
        'model_loaded': True if model else False
    }

@app.post('/predict', response_model=predictionResponse)
def predict_premium(data: UserInput):

    user_input =  {
            'bmi': data.bmi,
            'age_group': data.age_group,
            'lifestyle_risk': data.lifestyle_risk,
            'city_tier': data.city_tier,
            'income_lpa': data.income_lpa,
            'occupation': data.occupation
        }

    try:

            prediction = predict_output(user_input)

            return JSONResponse(status_code=200, content={'Response': prediction})

    except Exception as e:
            return JSONResponse(status_code=500, content={'error': str(e)})