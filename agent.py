from langchain.agents import create_agent
from tools import *
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

out = StrOutputParser()

def search_agent():
    return create_agent(
        model=llm,
        tools=[search_tool]
    )


def scrap_agent():
    return create_agent(
        model=llm,
        tools=[web_scrapper]
    )


from langchain_core.prompts import ChatPromptTemplate

writer_prompt = ChatPromptTemplate.from_messages([
    {
        "role": "system",
        "content": """You are an expert research writer.
        Write a complete research report based on the given topic
        and research material.

        Include:
        1. Title
        2. Abstract
        3. Introduction
        4. Research Objectives
        5. Literature Review
        6. Research Methodology
        7. Key Findings
        8. Discussion
        9. Limitations
        10. Conclusion
        11. References with source URLs

        Use clear academic language. Do not invent facts,
        findings, or references. Use only the provided research material."""
    },
    {
        "role": "user",
        "content": """Research Topic: {topic}

        Research Material: {research_gathered}

        Write a complete research report using this information."""
    }
])

writer_chain = writer_prompt | llm | out



review_prompt = ChatPromptTemplate.from_messages([
    {
        "role": "system",
        "content": """You are an expert research paper reviewer.

        Review the research report carefully and evaluate its quality.

        Assess the following criteria:
        1. Relevance to the research topic
        2. Abstract and introduction quality
        3. Literature review quality
        4. Research methodology
        5. Key findings and discussion
        6. Conclusion and limitations
        7. Structure, clarity, and academic writing
        8. References and supporting evidence

        Provide your review in the following format:

        1. Overall Rating: Give a score out of 10.
        2. Strengths: Explain what the report does well.
        3. Weaknesses: Identify missing, unclear, or weak sections.
        4. Limitations: Explain the limitations of the report and its research material.
        5. Accuracy and Evidence: Identify unsupported claims or missing evidence.
        6. Section-wise Review: Evaluate the important sections individually.
        7. Improvement Suggestions: Give specific, actionable suggestions.
        8. Final Verdict: State whether the report is excellent,
           good, needs improvement, or poor.

        Be objective, honest, and constructive.
        Do not invent facts or claim that you verified sources
        unless you actually have evidence to support that claim.
        Do not give a high score without sufficient justification.
        """
    },
    {
        "role": "user",
        "content": """Research Topic: {topic}

        Research Report:
        {report}

        Review this report and provide a score out of 10,
        along with strengths, weaknesses, limitations,
        and suggestions for improvement."""
    }
])

review_chain = review_prompt | llm |out
