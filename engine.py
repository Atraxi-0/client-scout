"""
engine.py
Updated LangGraph logic for ClientScout.
Uses the current 2026 'prompt' standard for create_react_agent.
"""

import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.utilities import DuckDuckGoSearchAPIWrapper
from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage, SystemMessage

# Load environment variables
load_dotenv()

@tool
def search_internet(query: str) -> str:
    """Searches the live internet."""
    print(f"DEBUG: Searching for -> {query}") # Add this line
    try:
        # Lower the max_results to 3 to speed it up for the demo
        wrapper = DuckDuckGoSearchAPIWrapper(max_results=3) 
        return wrapper.run(query)
    except Exception as e:
        return f"SEARCH FAILURE: {str(e)}"

def invoke_agent(company_name: str) -> str:
    """
    Initializes the LangGraph agent using the modern 'prompt' parameter.
    """
    # 1. Initialize LLM
    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0.2,
        max_tokens=1024
    )

    # 2. Define the rulebook as a SystemMessage
    # This is the most reliable way to enforce behavior in LangGraph 2026
    instructions = SystemMessage(content="""You are ClientScout, an elite B2B Intelligence Agent.
    Use the search_internet tool to research the requested company.
    
    OUTPUT STRUCTURE:
    ### [Company Name] Intelligence Report
    **1. Core Business:** [Summary]
    **2. Recent News:** [Developments]
    **3. IT Challenges:** [Technical analysis]
    """)

    # 3. Assemble the Agent
    # We use 'prompt' here as 'state_modifier' is now deprecated/removed
    agent = create_react_agent(
        model=llm, 
        tools=[search_internet], 
        prompt=instructions
    )

    # 4. Execute the Graph
    try:
        response = agent.stream({
            "messages": [HumanMessage(content=f"Research this company: {company_name}")]
        })
        
        return response["messages"][-1].content
        
    except Exception as e:
        return f"CRITICAL SYSTEM FAILURE: {str(e)}"