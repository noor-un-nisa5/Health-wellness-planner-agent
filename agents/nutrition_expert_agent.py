from utils.openai_mock import Agent

class NutritionExpertAgent(Agent):
    async def __call__(self, context):
        disease = (context.injury_notes or "").lower()

        
        if "diabetes" in disease or "diabetic" in disease or "شوگر" in disease:
            diet = [
                "Leafy green salads",
                "Whole grain roti",
                "Lentil (dal) soup",
                "Mixed vegetable stir fry",
                "Low-fat yogurt without sugar",
                "Nuts in moderation",
                "Bitter gourd juice"
            ]
            workouts = [
                "Light walking - 20 minutes",
                "Gentle yoga stretches",
                "Breathing exercises"
            ]
            note = "⚠️ Avoid: white rice, sugary sweets, processed snacks, mango, banana."

        
        elif "bp" in disease or "hypertension" in disease or "بی پی" in disease:
            diet = [
                "Oats with fruits",
                "Low-sodium vegetable soup",
                "Steamed fish or tofu",
                "Quinoa salad",
                "Banana (moderation)"
            ]
            workouts = [
                "Light yoga",
                "Walking - 30 minutes",
                "Deep breathing"
            ]
            note = "⚠️ Avoid: extra salt, pickles, fried food, canned items."

        
        elif "thyroid" in disease:
            diet = [
                "Boiled eggs",
                "Milk and yogurt",
                "Whole grains",
                "Nuts & seeds",
                "Green leafy vegetables (but limited cabbage, cauliflower)"
            ]
            workouts = [
                "Strength training (moderate)",
                "Brisk walk - 30 min",
                "Low-impact cardio"
            ]
            note = "⚠️ Avoid: excess soy products, raw cruciferous veggies."

        
        elif "migraine" in disease or "headache" in disease:
            diet = [
                "Fresh fruits (apple, pear)",
                "Green leafy vegetables",
                "Whole grains",
                "Lean proteins"
            ]
            workouts = [
                "Gentle stretching",
                "Breathing & relaxation exercises",
                "Short meditative walks"
            ]
            note = "⚠️ Avoid: caffeine, chocolate, aged cheese, processed meats."

        
        elif "sick" in disease or "ill" in disease:
            diet = [
                "Light khichdi (rice & dal)",
                "Vegetable soup",
                "Coconut water",
                "Steamed veggies",
                "Plain yogurt"
            ]
            workouts = [
                "Rest more",
                "Gentle breathing",
                "Slow stretching if no fever"
            ]
            note = "⚠️ Focus on rest and hydration."

        else:
            diet = ["Please consult with a specialist for your condition."]
            workouts = []
            note = ""

        return (
            f"🍎 Disease-specific Diet Plan: {diet}\n\n"
            f"🏃‍♀️ Suggested Workouts: {workouts}\n\n"
            f"{note}"
        )
