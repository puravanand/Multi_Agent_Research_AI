from bs4 import BeautifulSoup
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
import os
import requests
from langchain.tools import tool
from tavily import TavilyClient
from bs4 import BeautifulSoup
from rich import print
llm = ChatOpenAI(model="mistralai/mistral-large-2512", base_url="https://api.xkiro.com/v1")

tavily = TavilyClient()

@tool
def search_tool(topic:str) -> str:
    """Search the web for a topic and return relevant results with their titles, URLs, and content snippets."""
    result = tavily.search(query=topic, max_results=5)

    out=[]
    for r in result['results']:
        out.append(
        f"Title: {r['title']} \n URL: {r['url']} \n Snippet: {r['content']}")

    return "\n\n".join(out)



@tool
def web_scrapper(url : str) -> str:
        """Scrape a webpage and return its readable text content."""
        try:
             response = requests.get(url, timeout=8 , headers={"User-Agent":"Mozilla/5.0"})
             soup= BeautifulSoup(response.text , "html.parser")
             for tag in soup(["style","script" ,"nav","footer","header"]):
                  tag.decompose()

             return soup.get_text()

        except Exception as e:
             return f"Error{e}"


# print(web_scrapper.invoke("https://www.un.org/en/coronavirus"))



    


    
