from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class MyCrew():
    """MyCrew crew"""

    agents_config='config/agents.yaml'
    tasks_config='config/tasks.yaml'

    @agent
    def flight_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['flight_agent'], # type: ignore[index]
            verbose=True
        )

    @agent
    def hotel_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['hotel_agent'], # type: ignore[index]
            verbose=True
        )

    @agent
    def tour_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['tour_agent'], # type: ignore[index]
            verbose=True
        )

    @agent
    def advice_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['advice_agent'], # type: ignore[index]
            verbose=True
        )
    
    @agent
    def coordination_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['coordination_agent'], # type: ignore[index]
            verbose=True
        ) 

   
    @task
    def find_flight(self) -> Task:
        return Task(
            config=self.tasks_config['find_flight'], 
            output_file='flight_options.md'
        )

    @task
    def find_hotel(self) -> Task:
        return Task(
            config=self.tasks_config['find_hotel'], # type: ignore[index]
            output_file='hotel_options.md'
        )

    @task
    def plan_itinerary(self) -> Task:
        return Task(
            config=self.tasks_config['plan_itinerary'], # type: ignore[index]
            output_file='itinerary.md'
        )

    @task
    def give_advice(self) -> Task:
        return Task(
            config=self.tasks_config['give_advice'], # type: ignore[index]
            output_file='report.md'
        )
    @task
    def get_user_input(self) -> Task:
        return Task(
            config=self.tasks_config['get_user_input'], # type: ignore[index]
            output_file='user_input.md'
        )
    @task
    def compile_report(self) -> Task:
        return Task(
            config=self.tasks_config['compile_report'], # type: ignore[index]
            output_file='final_report.md'
        )



    @crew
    def crew(self) -> Crew:
        """Creates the MyCrew crew"""
        
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
