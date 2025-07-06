from utils.openai_mock import RunHooks

class MyHooks(RunHooks):
    async def on_tool_start(self, tool_name, context):
        print(f"Tool started: {tool_name}")

    async def on_tool_end(self, tool_name, context, output):
        print(f"Tool ended: {tool_name} — Output: {output}")

    async def on_handoff(self, from_agent, to_agent, context):
        print(f"Handoff from {from_agent} to {to_agent}")
