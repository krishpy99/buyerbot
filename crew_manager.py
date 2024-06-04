from crewai import Crew

from agents import researcher, writer
from tasks import task1, task2

crew = Crew(agents=[researcher, writer], tasks=[task1, task2], verbose=2)

task_output = crew.kickoff()
print(task_output)