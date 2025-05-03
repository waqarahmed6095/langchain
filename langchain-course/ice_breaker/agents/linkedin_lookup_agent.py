import os
import sys
from pathlib import Path
from typing import Optional

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import Tool
from langchain_ollama import ChatOllama

from langchain import hub
from langchain.agents import AgentExecutor, create_react_agent

# Add the parent directory to sys.path to make imports work when running directly
sys.path.append(str(Path(__file__).parent.parent))
from tool.tools import get_profile_url_tavily

load_dotenv()


def lookup(name: str) -> str:
    llm = ChatOllama(model="qwen3:4b", temperature=0)
    template = """Given the full name {name_of_person} I want you ti get it me a link to their Linkedin profile page.
    Your answer should contain only a URL. /no_think"""
    prompt_template = PromptTemplate(
        input_variables=["name_of_person"], template=template
    )
    tools_for_agent = [
        Tool(
            name="Crawl Google 4 linkedin profile page",
            func=get_profile_url_tavily,
            description="useful for when you need get the Linkedn Page URL",
        )
    ]

    react_prompt = hub.pull("hwchase17/react")
    react_prompt += " /no_think"
    agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)
    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools_for_agent,
        verbose=True,
        handle_parsing_errors=True,  # Added this parameter
    )
    result = agent_executor.invoke(
        input={"input": prompt_template.format_prompt(name_of_person=name)}
    )
    linkedin_profile_url = result["output"]
    return linkedin_profile_url


if __name__ == "__main__":
    lookup(name="Abdul Moeed Bilkent University ")  # Example name
