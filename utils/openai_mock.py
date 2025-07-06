from types import SimpleNamespace

class Tool:
    name = "generic_tool"

    def __init__(self):
        pass

    async def __call__(self, *args, **kwargs):
        return "Tool called!"

class Agent:
    def __init__(self, tools=None, handoffs=None):
        self.tools = {tool.name: tool for tool in (tools or [])}
        self.handoffs = {agent.name: agent for agent in (handoffs or [])}

    def get_tool(self, name):
        return self.tools.get(name)

    async def handoff(self, agent_name, context):
        agent = self.handoffs.get(agent_name)
        if agent:
            return await agent(context)
        else:
            return f"No agent found for handoff: {agent_name}"

class Runner:
    def __init__(self, hooks=None):
        self.hooks = hooks

    async def stream(self, starting_agent, input, context):
        
        output = await starting_agent(input, context)
        for line in str(output).splitlines():
            yield SimpleNamespace(pretty_output=line)

class RunHooks:
    async def on_tool_start(self, tool_name, context):
        pass

    async def on_tool_end(self, tool_name, context, output):
        pass

    async def on_handoff(self, from_agent, to_agent, context):
        pass
