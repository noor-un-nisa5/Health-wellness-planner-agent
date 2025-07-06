from utils.openai_mock import Tool

class MealPlannerTool(Tool):
    name = "meal_planner"

    async def __call__(self, input_text, context):
        
        if not context.goal:
            return {"vegetarian": [], "non_vegetarian": []}

        objective = context.goal["objective"]

        
        if objective == "lose":
            vegetarian = [
                "Oats porridge with berries",
                "Mixed vegetable salad with lemon dressing",
                "Grilled paneer with steamed broccoli",
                "Lentil soup with whole grain toast",
                "Stuffed cucumber rolls with hummus",
                "Low-fat yogurt with flax seeds",
                "Green smoothie with spinach and apple"
            ]
            non_vegetarian = [
                "Grilled chicken breast with green salad",
                "Steamed fish with asparagus",
                "Egg white omelette with spinach",
                "Chicken soup with veggies",
                "Tuna salad with avocado",
                "Grilled shrimp with quinoa",
                "Turkey lettuce wraps"
            ]
        
        elif objective == "gain":
            vegetarian = [
                "Peanut butter banana smoothie",
                "Paneer paratha with yogurt",
                "Mixed nuts and dried fruits bowl",
                "Lentil curry with rice",
                "Whole grain pasta with vegetables and cheese",
                "Avocado and chickpea sandwich",
                "Protein shake with almond milk"
            ]
            non_vegetarian = [
                "Chicken and rice bowl with veggies",
                "Salmon with creamy mashed potatoes",
                "Egg and cheese sandwich with avocado",
                "Beef stir fry with rice noodles",
                "Chicken curry with naan",
                "Shrimp pasta with olive oil",
                "Greek yogurt with honey and mixed fruits"
            ]
        else:
            vegetarian = []
            non_vegetarian = []

        return {"vegetarian": vegetarian, "non_vegetarian": non_vegetarian}
