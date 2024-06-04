import os
from crewai import Agent
from crewai_tools import SerperDevTool
from langchain_community.llms import Ollama

os.environ["SERPER_API_KEY"] = "a267dc1a84ac133e64128608f08910cf27d4f8b1"

llm = Ollama(model="openhermes")

search_tool = SerperDevTool()

researcher = Agent(
    llm=llm,
    role="Senior Property Researcher",
    goal="Find promising investment properties.",
    backstory="You are a veteran property analyst. In this case you're looking for retail properties to invest in.",
    allow_delegation=False,
    tools=[search_tool],
    verbose=True,
)



writer = Agent(
    llm=llm,
    role="Senior Property Analyst",
    goal="Summarise property facts into a report for investors.",
    backstory="You are a real estate agent, your goal is to compile property analytics into a report for potential investors.",
    allow_delegation=False,
    verbose=True,
)