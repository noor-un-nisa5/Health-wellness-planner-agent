from guardrails import GoalInput

class GoalAnalyzerTool:
    async def __call__(self, user_input: str) -> dict:
        
        user_input = user_input.lower()

        
        objective = "lose"
        quantity = 5
        unit = "kg"
        duration = "2 months"


        if "gain" in user_input or "weight gain" in user_input:
            objective = "gain"
        elif "lose" in user_input:
            objective = "lose"
        elif "maintain" in user_input:
            objective = "maintain"

        
        import re
        q_match = re.search(r'(\d+(\.\d+)?)', user_input)
        if q_match:
            quantity = float(q_match.group(1))

        
        if "kg" in user_input:
            unit = "kg"
        elif "lb" in user_input or "lbs" in user_input:
            unit = "lbs"

        
        if "month" in user_input:
            duration = "2 months"  
            d_match = re.search(r'(\d+)\s*month', user_input)
            if d_match:
                duration = f"{d_match.group(1)} months"
        elif "week" in user_input:
            duration = "2 weeks"
            d_match = re.search(r'(\d+)\s*week', user_input)
            if d_match:
                duration = f"{d_match.group(1)} weeks"
        elif "year" in user_input:
            duration = "1 year"
            d_match = re.search(r'(\d+)\s*year', user_input)
            if d_match:
                duration = f"{d_match.group(1)} years"

        
        goal = GoalInput(
            objective=objective,
            quantity=quantity,
            unit=unit,
            duration=duration
        )

        
        return goal.dict()


