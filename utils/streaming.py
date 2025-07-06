async def stream_runner(runner, agent, input_text, context):
    async for step in runner.stream(starting_agent=agent, input=input_text, context=context):
        print(step.pretty_output)
