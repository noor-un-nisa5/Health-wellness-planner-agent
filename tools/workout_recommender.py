from utils.openai_mock import Tool

class WorkoutRecommenderTool(Tool):
    name = "workout_recommender"

    async def __call__(self, input_text, context):
        if not context.goal:
            return []

        objective = context.goal["objective"]

        if objective == "lose":
            workouts = [
                "Jump rope - 10 min",
                "HIIT circuit - 20 min",
                "Treadmill running - 30 min",
                "Mountain climbers - 3 sets x 20 reps",
                "Burpees - 3 sets x 15 reps",
                "Cycling - 45 min",
                "Core strengthening - 15 min"
            ]
        elif objective == "gain":
            workouts = [
                "Deadlifts - 4 sets x 8 reps",
                "Bench press - 4 sets x 10 reps",
                "Squats with weights - 4 sets x 12 reps",
                "Pull-ups - 3 sets x 8 reps",
                "Barbell rows - 3 sets x 10 reps",
                "Shoulder press - 3 sets x 12 reps",
                "Leg press - 4 sets x 10 reps"
            ]
        else:
            workouts = []

        return workouts
