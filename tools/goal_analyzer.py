from guardrails import GoalInput

class GoalAnalyzerTool:
    async def __call__(self, user_input: str) -> GoalInput:
        user_input = user_input.lower()

        if "gain" in user_input:
            objective = "gain"
        elif "maintain" in user_input:
            objective = "maintain"
        else:
            objective = "lose"

        
        import re
        q_match = re.search(r'(\d+(\.\d+)?)', user_input)
        quantity = float(q_match.group(1)) if q_match else 5

        if "kg" in user_input:
            unit = "kg"
        elif "lb" in user_input or "lbs" in user_input:
            unit = "lbs"
        else:
            unit = "kg"

        if "month" in user_input:
            d_match = re.search(r'(\d+)\s*month', user_input)
            duration = f"{d_match.group(1)} months" if d_match else "2 months"
        elif "week" in user_input:
            d_match = re.search(r'(\d+)\s*week', user_input)
            duration = f"{d_match.group(1)} weeks" if d_match else "2 weeks"
        else:
            duration = "2 months"

        goal = GoalInput(
            objective=objective,
            quantity=quantity,
            unit=unit,
            duration=duration
        )

        return goal


