import pandas as pd
from fastapi import HTTPException
from backend.model_loader import model, FEATURE_RANGES

EXPECTED_COLUMNS = [
    'CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE',
    'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT'
]

def check_input_ranges(input_dict):
    warnings = []
    for col, (low, high) in FEATURE_RANGES.items():
        value = input_dict.get(col)
        if value is None:
            continue  
        if value < low or value > high:
            warnings.append(f"{col}={value} outside expected range [{low:.2f}, {high:.2f}]")
    return warnings

def predict_price(data):
    input_dict = data.dict()
    
    missing_fields = [col for col, val in input_dict.items() if val is None]

    df = pd.DataFrame([input_dict])
    df = df[EXPECTED_COLUMNS] 

    prediction = model.predict(df)

    warnings = check_input_ranges(df.iloc[0].to_dict())

    response = {
        "predicted_house_price": round(float(prediction[0]), 2),
        "missing_fields": missing_fields,
        "warnings": warnings
    }
    return response
