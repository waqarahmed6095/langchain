from dotenv import load_dotenv
from langchain_community.tools.tavily_search import TavilySearchResults

load_dotenv()


def get_profile_url_tavily(name: str):
    """Searches for Linkedin or Twitter Profile Page."""
    search = TavilySearchResults()
    res = search.run(f"{name}")
    return res


if __name__ == "__main__":
    search = get_profile_url_tavily("Waqar Ahmed Jamali Koc university")

    print(search)
