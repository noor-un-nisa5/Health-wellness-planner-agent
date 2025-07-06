from pydantic import BaseModel, validator

class GoalInput(BaseModel):
    quantity: float
    unit: str
    duration: str

    @validator("quantity")
    def quantity_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError("Quantity must be positive")
        return v

    @validator("unit")
    def unit_supported(cls, v):
        allowed_units = ["kg", "lbs"]
        if v not in allowed_units:
            raise ValueError(f"Unit must be one of {allowed_units}")
        return v

    @validator("duration")
    def duration_format(cls, v):
        
        allowed_words = ["week", "weeks", "month", "months", "year", "years"]
        if not any(word in v for word in allowed_words):
            raise ValueError("Duration must mention time unit like weeks or months")
        return v

