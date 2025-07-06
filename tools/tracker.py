from utils.openai_mock import Tool

class ProgressTrackerTool(Tool):
    name = "tracker"

    async def __call__(self, input_text, context):
        context.progress_logs.append({"update": input_text})
        return "Your progress has been logged!"
