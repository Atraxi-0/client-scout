import streamlit as st
from engine import invoke_agent

# Page Config for a professional look
st.set_page_config(page_title="ClientScout | B2B Intelligence", page_icon="🔍")

def main():
    st.title("🔍 ClientScout")
    st.subheader("Autonomous B2B Intelligence Agent")
    st.markdown("---")

    # User Input
    company_name = st.text_input("Enter Company Name:", placeholder="e.g. NVIDIA, Microsoft, Zomato")

    if st.button("Generate Intelligence Report"):
        if not company_name:
            st.warning("Please enter a company name.")
            return

        with st.spinner(f"Agent is researching {company_name}... (Searching live web)"):
            try:
                # Calls your existing LangGraph logic
                report = invoke_agent(company_name)
                
                st.success("Report Generated!")
                st.markdown(report)
                
            except Exception as e:
                st.error(f"An error occurred: {e}")

    # Sidebar info for recruiters
    with st.sidebar:
        st.header("About ClientScout")
        st.info("""
        **Tech Stack:**
        - LangGraph (ReAct DAG)
        - Groq (Llama-3.3-70B)
        - DuckDuckGo Search
        - Streamlit
        """)
        st.markdown("Developed by: Krishna Kant Pathak")

if __name__ == "__main__":
    main()