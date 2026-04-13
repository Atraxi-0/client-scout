# 🔍 ClientScout: Autonomous B2B Intelligence Agent

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![LangGraph](https://img.shields.io/badge/LangGraph-Stateful_Agent-orange.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-red.svg)
![Groq](https://img.shields.io/badge/Groq-Llama_3-black.svg)

ClientScout is a autonomous Artificial Intelligence agent designed for high-speed B2B market research. Built on a Directed Acyclic Graph (DAG) architecture using **LangGraph**, the agent dynamically navigates the live internet to extract, synthesize, and format corporate intelligence into professional reports.

---

## 🚀 Key Features

- **Stateful ReAct Architecture:** Utilizes LangGraph to maintain a persistent memory state during the reasoning loop, allowing the agent to self-correct tool-calling errors and refine its search strategy dynamically.
- **Autonomous Web Research:** Integrates DuckDuckGo API to actively scour the internet for real-time corporate data, bypassing the limitations of static LLM training cutoffs.
- **Self-Healing Execution:** Engineered with recursion limits and custom system constraints to automatically recover from LLM hallucinations (e.g., XML formatting errors) without crashing the application.
- **Production-Ready UI:** Deployed via Streamlit Community Cloud for a responsive, professional, and accessible user interface.
- **Graceful Error Handling:** Built-in safeguards against API rate limits and search failures to ensure a seamless user experience.

---

## 🛠️ Tech Stack

- **Core Framework:** LangGraph, LangChain Core
- **Large Language Model:** Llama-3.3-70B / Llama-3.1-8B (via Groq API)
- **Web Search Tool:** DuckDuckGo Search API Wrapper
- **Frontend / Deployment:** Streamlit / Streamlit Community Cloud
- **Language:** Python

---

## 📂 Project Architecture

The application enforces a strict separation of concerns:

- `engine.py`: The "Brain". Contains the LangGraph workflow, system prompts, tool definitions, and LLM initialization. Handles the iterative reasoning loop and data cleaning.
- `app.py`: The "Face". The Streamlit web application that manages user inputs, session states, visual rendering of the Markdown report, and error shielding.
- `requirements.txt`: The explicit dependency manifest for CI/CD cloud deployment.

---

## 💻 Local Installation

To run ClientScout locally, follow these steps:

1. **Clone the repository**
   ```bash
   git clone [https://github.com/your-username/ClientScout.git](https://github.com/your-username/ClientScout.git)
   cd ClientScout
   ```

2. **Set up your environment variables**
   Create a `.env` file in the root directory and add your Groq API key:
   ```env
   GROQ_API_KEY=your_actual_api_key_here
   ```

3. **Install the dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Launch the application**
   ```bash
   streamlit run app.py
   ```
   *The application will open in your default web browser at `http://localhost:8501`.*

---

## 🎯 Usage

1. Open the ClientScout web interface.
2. Enter the name of a target company (e.g., "NVIDIA", "HighRadius", "Zomato").
3. Click **Generate Intelligence Report**.
4. The agent will autonomously search the web and return a 3-point Markdown report detailing:
   - Core Business & Value Proposition
   - Recent Strategic Developments
   - Probable IT & Operational Challenges

---

## 👨‍💻 Author

**Krishna Kant Pathak**
*Lead Architect & Full-Stack Developer*

*Developed as a high-performance B2B intelligence tool emphasizing modern agentic workflows and reliable cloud deployment.*
