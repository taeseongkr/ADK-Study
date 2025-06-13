from google.adk.agents import Agent
from google.adk.tools import google_search

def my_tool_function(query):
    # This function can be used to process the query before passing it to the tool
    return query

root_agent = Agent(
    name="tool_agent",
    description="Search agent",
    instruction="""
    You are a search agent that uses Google Search to find information.
    When the user asks a question, use the Google Search tool to find relevant information.
    """,
    tools=[google_search],
    model="gemini-2.0-flash")

