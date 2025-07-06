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

class MealPlanOutput(BaseModel):
    meals: list

class WorkoutPlanOutput(BaseModel):
    workouts: list
