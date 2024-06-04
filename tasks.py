from crewai import Task
from agents import researcher, writer

task1 = Task(
    description="Search the internet and find 5 promising real estate investment suburbs in Sydney, Australia. For each suburb highlighting the mean, low and max prices as well as the rental yield and any potential factors that would be useful to know for that area.",
    expected_output="""A detailed report of each of the suburbs.The results should be formatted as shown below: 

    Suburb 1: Randosuburbville
    Mean Price: $1,200,000
    Rental Vacancy: 4.2%
    Rental Yield: 2.9%
    Background Information: These suburbs are typically located near major transport hubs, employment centers, and educational institutions. The following list highlights some of the top contenders for investment opportunities """,
    agent=researcher,
    output_file="task1_output.txt",
)

task2 = Task(
    description="Summarise the property information into bullet point list. ",
    expected_output="A summarised dot point list of each of the suburbs, prices and important features of that suburb.",
    agent=writer,
    output_file="task2_output.txt",
)