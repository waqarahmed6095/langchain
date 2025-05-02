import os
import requests
from dotenv import load_dotenv

load_dotenv()


def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False):
    """scrape information from LinkedIn profiles,
    Manuall scrape the information from the LinkedIn profile"""
    if mock:
        linkedin_profile_url = (
            "https://gist.github.com/waqarahmed6095/d4fb7f3a1792962645a5b80676c5b2d0"
        )
        response = requests.get(linkedin_profile_url, timeout=10)
    else:
        api_endpoint ="https://api.scrapin.io/enrichment/profile"
        params


if __name__ == "__main__":
    print(
        scrape_linkedin_profile(
            linkedin_profile_url="https://www.linkedin.com/in/eden-marco/"
        )
    )
