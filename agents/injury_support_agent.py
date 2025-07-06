from utils.openai_mock import Agent

class InjurySupportAgent(Agent):
    name = "injury_support_agent"

    async def __call__(self, context):
        return "Here’s a safe workout plan considering your injury. Please follow carefully."
