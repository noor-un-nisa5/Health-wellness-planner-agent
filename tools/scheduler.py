from utils.openai_mock import Tool

class CheckinSchedulerTool(Tool):
    name = "scheduler"

    async def __call__(self, input_text, context):
        return "Weekly check-in scheduled for the next 12 weeks to monitor weight and meal compliance."

