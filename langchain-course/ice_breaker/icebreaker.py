from agents.linkedin_lookup_agent import lookup
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from third_parties.linkedn import scrape_linkedin_profile


def ice_break_with(name: str):
    linkedin_username = lookup(name=name)
    linkedin_data = scrape_linkedin_profile(linkedin_username)
    summary_template = """
         given the information about a person from linkedin {information},  I want you to create:
         1. a short summary
         2. two interesting facts about them

        /no_think.
     """

    summary_prompt_template = PromptTemplate(
        input_variables="information", template=summary_template
    )

    llm = ChatOllama(temperature=0, model="qwen3:4b", extract_reasoning=False)
    chain = summary_prompt_template | llm | StrOutputParser()

    res = chain.invoke(input={"information": linkedin_data})

    print(res)


if __name__ == "__main__":
    print("Ice Breaker Enter ")

    load_dotenv()

    ice_break_with(name="Waqar Ahmed Kentkart Koc University")  # Example name