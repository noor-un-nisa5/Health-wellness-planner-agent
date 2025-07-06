import re
from .guardrails import GoalInput
from utils.openai_mock import Tool

class GoalAnalyzerTool(Tool):
    name = "goal_analyzer"

    async def __call__(self, input_text: str) -> GoalInput:
        input_text = input_text.lower()
        
        if "lose" in input_text:
            objective = "lose"
        elif "gain" in input_text:
            objective = "gain"
        else:
            raise ValueError("Please specify if you want to 'lose' or 'gain' weight.")
        
        quantity_match = re.search(r"(\d+)\s*(kg|lbs)", input_text)
        if not quantity_match:
            raise ValueError("Please mention a target weight, e.g., '5 kg' or '10 lbs'.")
        quantity = float(quantity_match.group(1))
        unit = quantity_match.group(2)
        
        duration_match = re.search(r"in\s+(\d+\s+\w+)", input_text)
        if not duration_match:
            duration = "3 months" 
        else:
            duration = duration_match.group(1)
        
        return GoalInput(objective=objective, quantity=quantity, unit=unit, duration=duration)
