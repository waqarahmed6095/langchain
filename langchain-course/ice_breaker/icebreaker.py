from typing import Tuple

from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from agents.twitter_lookup_agent import lookup as twitter_lookup_agent
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from output_parsers import Summary, summary_parser
from third_parties.linkedn import scrape_linkedin_profile
from third_parties.twitter import scrape_user_tweets


def ice_break_with(name: str) -> Tuple[Summary, str]:
    linkedin_username = linkedin_lookup_agent(name=name)
    linkedin_data = scrape_linkedin_profile(linkedin_username)
    twitter_username = twitter_lookup_agent(name=name)
    tweets = scrape_user_tweets(username=name)
    summary_template = """
         given the information about a person from linkedin {information}, and latest twitter posts {twitter_posts} I want you to create:
         1. a short summary
         2. two interesting facts about them

         Use both information from twitter and linkedn \n {format_instructions}
        /no_think.
     """

    summary_prompt_template = PromptTemplate(
        input_variables=["information", "twitter_posts"],
        template=summary_template,
        partial_variables={
            "format_instructions": summary_parser.get_format_instructions()
        },
    )

    llm = ChatAnthropic(model="claude-3-5-sonnet-20241022", temperature=0)

    chain = summary_prompt_template | llm | summary_parser

    res: Summary = chain.invoke(
        input={"information": linkedin_data, "twitter_posts": tweets}
    )
    print(linkedin_data.get("photoUrl"))

    return res, linkedin_data.get("photoUrl")


if __name__ == "__main__":
    print("Ice Breaker Enter ")

    load_dotenv()

    ice_break_with(name="Eden Marco Udemy")  # Example name
