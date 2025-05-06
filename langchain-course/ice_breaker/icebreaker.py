from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from agents.twitter_lookup_agent import lookup as twitter_lookup_agent
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from third_parties.linkedn import scrape_linkedin_profile
from third_parties.twitter import scrape_user_tweets


def ice_break_with(name: str):
    linkedin_username = linkedin_lookup_agent(name=name)
    linkedin_data = scrape_linkedin_profile(linkedin_username)
    twitter_username = twitter_lookup_agent(name=name)
    tweets = scrape_user_tweets(username=twitter_username)
    summary_template = """
         given the information about a person from linkedin {information}, and latest twitter posts {twitter_posts} I want you to create:
         1. a short summary
         2. two interesting facts about them

         Use both information from twitter and linkedn
        /no_think.
     """

    summary_prompt_template = PromptTemplate(
        input_variables=["information","twitter_posts"], template=summary_template
    )

    llm = ChatOllama(temperature=0, model="qwen3:4b", extract_reasoning=False)
    chain = summary_prompt_template | llm | StrOutputParser()

    res = chain.invoke(input={"information": linkedin_data,"twitter_posts":tweets})

    print(res)


if __name__ == "__main__":
    print("Ice Breaker Enter ")

    load_dotenv()

    ice_break_with(name="Soomal Jamali TRDP")  # Example name
