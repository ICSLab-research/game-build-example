import os
from config import Config
from textwrap import dedent

from crewai import Crew
from src.llms.llm import LLMs
from src.tasks.task import GameTasks
from src.agents.agent import GameAgents

os.environ["OPENAI_API_KEY"] = "NA"

game = description = dedent(
    """\
    Develop a basic Pong game using Python. The game should have:
        - Two paddles controlled by players.
        - A ball that bounces off the paddles and walls.
        - A scoring system to keep track of points.
        - Simple graphics and controls.
    """
)

llms = LLMs()
agents = GameAgents()
tasks = GameTasks()

print("DEFAULT_LLM:", Config.DEFAULT_LLM)
# print("CODER_LLM:", Config.CODER_LLM)

default_llm = llms.get_llm(model=Config.DEFAULT_LLM)
# coder_llm = llms.get_llm(model=Config.CODER_LLM)

senior_engineer_agent = agents.senior_engineer_agent(llm=default_llm)
qa_engineer_agent = agents.qa_engineer_agent(llm=default_llm)
chief_qa_engineer_agent = agents.chief_qa_engineer_agent(llm=default_llm)

code_task = tasks.code_task(senior_engineer_agent)
review_task = tasks.review_task(qa_engineer_agent)
evaluate_task = tasks.evaluate_task(chief_qa_engineer_agent)

crew = Crew(
    tasks=[
        code_task,
        review_task,
        evaluate_task,
    ],
    agents=[
        senior_engineer_agent,
        qa_engineer_agent,
        chief_qa_engineer_agent,
    ],
    verbose=True,
    memory=True,
    embedder={
        "provider": "ollama",
        "config": dict(
            model="nomic-embed-text",
        ),
    },
)

result = crew.kickoff({"game": game})

print(result)
