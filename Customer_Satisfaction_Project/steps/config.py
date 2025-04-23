from pydantic import BaseModel  # Changed import

class ModelNameConfig(BaseModel):  # Inherit from Pydantic's BaseModel
    model_name: str = "LinearRegression"