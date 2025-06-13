from google.adk.agents import Agent

root_agent = Agent(
    name="greeting_agent",
    model="gemini-2.0-flash",
    description="A simple agent that greets the user.",
    instruction="""
    You are a friendly agent that greets the user.
    When the user says 'hello', respond with a greeting.
    If the user says 'bye', respond with a farewell.
    If the user says anything else, respond with a question asking how you can help.
    """,
    )

