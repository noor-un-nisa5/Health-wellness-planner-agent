from utils.openai_mock import Agent
from tools.goal_analyzer import GoalAnalyzerTool
from tools.meal_planner import MealPlannerTool
from tools.workout_recommender import WorkoutRecommenderTool
from tools.scheduler import CheckinSchedulerTool
from tools.tracker import ProgressTrackerTool
from agents.escalation_agent import EscalationAgent
from agents.nutrition_expert_agent import NutritionExpertAgent
from agents.injury_support_agent import InjurySupportAgent

class HealthWellnessPlannerAgent(Agent):
    def __init__(self):
        self.goal_tool = GoalAnalyzerTool()
        self.meal_tool = MealPlannerTool()
        self.workout_tool = WorkoutRecommenderTool()
        self.scheduler_tool = CheckinSchedulerTool()
        self.tracker_tool = ProgressTrackerTool()
        self.handoffs = {
            "EscalationAgent": EscalationAgent(),
            "NutritionExpertAgent": NutritionExpertAgent(),
            "InjurySupportAgent": InjurySupportAgent(),
        }

    async def __call__(self, input_text, context):
        input_text_lower = input_text.lower()

        
        disease_keywords = [
            "diabetes", "diabetic",
            "bp", "hypertension", 
            "thyroid", 
            "migraine", "headache",
            "sick", "ill", 
        ]

        if any(keyword in input_text_lower for keyword in disease_keywords):
            context.injury_notes = input_text_lower
            return await self.handoffs["NutritionExpertAgent"](context)

        
        if "lose" in input_text_lower or "gain" in input_text_lower:
            goal = await self.goal_tool(input_text)
            context.goal = goal.dict()

            meal_plan = await self.meal_tool(input_text, context)
            context.meal_plan = meal_plan

            workout_plan = await self.workout_tool(input_text, context)
            context.workout_plan = workout_plan

            schedule = await self.scheduler_tool(input_text, context)
            tracker_msg = await self.tracker_tool(f"Tracking progress for {goal.quantity} {goal.unit} in {goal.duration}", context)

            trainer_msg = ""
            if goal.quantity >= 20:
                trainer_msg = await self.handoffs["EscalationAgent"](context)

            final_response = (
                f"🎯 Goal: {context.goal}\n\n"
                f"🥗 Meal Plan: {meal_plan}\n\n"
                f"💪 Workout Plan: {workout_plan}\n\n"
                f"📅 Schedule: {schedule}\n\n"
                f"✅ Tracker: {tracker_msg}\n\n"
                f"{trainer_msg}"
            )
            return final_response

        return "❓ Please provide your goal (e.g., 'I want to lose 10 kg in 3 months') or mention your condition (e.g., 'I am diabetic')."
