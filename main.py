from tools import*
from agent import*

def run_pipeline(topic :str)-> dict:
    all_result={}
    print("\n Search Agent is working..\n")
    search_agent_instance=search_agent()
    search_result=search_agent_instance.invoke({
                         "messages": [
            {
                "role": "user",
                "content": f"""You are an expert web research agent.
                Search for the given topic: {topic}

                Find the top 5 most relevant search results.
                For each result, provide:
                1. Title
                2. URL
                3. Short content snippet

                Return all 5 results clearly, keeping their original URLs."""
            }
        ]
                         
                         })
    all_result['search_result'] = search_result["messages"][-1].content
    print(all_result['search_result'])
    print("\n..................\n")

    print("\n Scrap Agent is working..\n")
    scrap_agent_instance=scrap_agent()
    web_result = scrap_agent_instance.invoke({
    "messages": [
        {
            "role": "user",
            "content": f"""You are an expert web scraping agent.

            Here are the search results for the topic: {topic}

            Search Results:
            {all_result["search_result"]}

            Select the most relevant URLs that are likely to contain
            detailed and useful information about the topic.

            Use the web_scrapper tool to extract the readable content
            from those URLs.

            Return the page title, URL, and extracted content for
            each successfully scraped webpage.
            Prefer reliable sources and content directly related
            to the research topic."""
        }]
    })

    all_result["web_result"] = web_result["messages"][-1].content
    print(all_result['web_result'])
    print("\n..................\n")   
    research_gathered = (
    all_result["search_result"]
    + "\n\n"
    + all_result["web_result"]
    )
    print("\n Writing Agent is working..\n")
   
    report=writer_chain.invoke({"topic":topic,"research_gathered":research_gathered})
    all_result['report']= report
    print("\n Ranking Agent is working..\n")
    print(all_result['report'])
    print("\n..................\n")
    ranking = review_chain.invoke({"topic":topic,"report":all_result['report']})
    all_result["ranking"] = ranking
    print(all_result['ranking'])
    print("\n..................\n")
    return all_result


if __name__ == "__main__":
    topic=input("Ask any research Topic:- ")
    result = run_pipeline(topic)
    print(result)