"""
engine.py
Core LangChain logic for the ClientScout B2B Intelligence Agent.
Handles LLM initialization, tool binding, and ReAct loop execution.
"""

import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.utilities import DuckDuckGoSearchAPIWrapper
from langchain_core.tools import tool
from langchain_core.prompts import ChatPromptTemplate
from langchain.agents import create_tool_calling_agent, AgentExecutor

# Load environment variables (GROQ_API_KEY)
load_dotenv()

@tool
def search_internet(query: str) -> str:
    """

    Searches the live internet for recent news and business information.
    Required for accurate B2B intelligence gathering.
    """
    try:
        wrapper = DuckDuckGoSearchAPIWrapper(max_results=5)
        return wrapper.run(query)
    except Exception as e:
        # Graceful degradation: If DDG fails, inform the LLM so it doesn't crash the loop
        return f"SEARCH PIPELINE FAILURE. Fallback to base knowledge. Error: {str(e)}"

def invoke_agent(company_name: str) -> str:
    """
    Initializes the agent and executes the Web-RAG loop for a given company.
    
    Args:
        company_name (str): The target B2B company to research.
        
    Returns:
        str: A formatted 3-point Markdown report.
    """
    # 1. Initialize LLM
    # Using Llama-3 70B for superior reasoning and JSON/tool-calling adherence
    llm = ChatGroq(
        model="llama3-70b-8192",
        temperature=0.2,
        max_tokens=1024
    )

    # 2. Bind Tools
    tools = [search_internet]

    # 3. Construct the Tool-Calling Prompt
    prompt = ChatPromptTemplate.from_messages([
        ("system", """You are ClientScout, an elite Autonomous B2B Intelligence Agent. 
        Your directive is to research the requested company using the search_internet tool and generate a precise, structured report.
        
        OUTPUT CONSTRAINTS - YOU MUST RETURN EXACTLY THIS MARKDOWN STRUCTURE:
        
        ### [Company Name] Intelligence Report
        **1. Core Business:** [1-2 sentences on what they sell and their target market]
        **2. Recent News:** [2-4 sentences on recent developments, funding, or product launches]
        **3. IT Challenges:** [2-4 sentences predicting likely technical or scale challenges they face based on their industry]
        """),
        ("human", "Research this company and generate the report: {input}"),
        ("placeholder", "{agent_scratchpad}"),
    ])

    # 4. Assemble the LCEL Agent
    agent = create_tool_calling_agent(llm, tools, prompt)
    
    # 5. Initialize the Executor
    agent_executor = AgentExecutor(
        agent=agent, 
        tools=tools, 
        verbose=False, # Suppressed to keep CLI clean; error handling is caught in the tool
        handle_parsing_errors=True
    )

    # 6. Execute the Chain
    try:
        response = agent_executor.invoke({"input": company_name})
        return response.get("output", "Error: Agent returned an empty response.")
    except Exception as e:
        return f"CRITICAL SYSTEM FAILURE: Agent execution aborted. Details: {str(e)}"