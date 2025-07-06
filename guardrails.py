from pydantic import BaseModel, validator

class GoalInput(BaseModel):
    objective: str
    quantity: float
    unit: str
    duration: str

    @validator("objective", "unit", "duration")
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError("Field cannot be empty")
        return v

    @validator("quantity")
    def quantity_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError("Quantity must be positive")
        return v

class MealPlanOutput(BaseModel):
    meals: list[str]

class WorkoutPlanOutput(BaseModel):
    workouts: list[str]




