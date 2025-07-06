from utils.openai_mock import Agent

class EscalationAgent(Agent):
    name = "escalation_agent"

    async def __call__(self, context):
        return "You are now connected with a human trainer!"
