import os
from crewai import Agent
from crewai_tools import SerperDevTool
from dotenv import dotenv_values

config = dotenv_values(".env")

os.environ["SERPER_API_KEY"] = config["SERPER_KEY"]
os.environ["OPENAI_API_KEY"] = config["OPENAI_KEY"]

search_tool = SerperDevTool()

researcher = Agent(
    role="Senior Property Researcher",
    goal="Find promising investment properties.",
    backstory="You are a veteran property analyst. In this case you're looking for retail properties to invest in.",
    allow_delegation=True,
    tools=[search_tool],
    verbose=True,
)

writer = Agent(
    role="Senior Property Analyst",
    goal="Summarise property facts into a report for investors.",
    backstory="You are a real estate agent, your goal is to compile property analytics into a report for potential investors.",
    allow_delegation=True,
    verbose=True,
)