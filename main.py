import asyncio
from agent import HealthWellnessPlannerAgent
from context import UserSessionContext
from utils.openai_mock import Runner
from hooks import MyHooks

async def main():
    context = UserSessionContext(name="User", uid=1)
    agent = HealthWellnessPlannerAgent()
    runner = Runner(hooks=MyHooks())

    print("🤖 Welcome to your Health & Wellness Planner!")
    print("Type 'exit' anytime to quit.\n")

    while True:
        input_text = input("How can I assist you with your health today?\n> ")

        if input_text.lower() in ["exit", "quit"]:
            print("👋 Goodbye! Stay healthy!")
            break

        async for step in runner.stream(starting_agent=agent, input=input_text, context=context):
            print(step.pretty_output)

if __name__ == "__main__":
    asyncio.run(main())
