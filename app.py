import streamlit as st
from engine import invoke_agent

# Page Config
st.set_page_config(page_title="ClientScout | B2B Intelligence", page_icon="🔍")

def main():
    st.title("🔍 ClientScout")
    st.subheader("Autonomous B2B Intelligence Agent")
    st.markdown("---")

    # User Input
    company_name = st.text_input("Enter Company Name:", placeholder="e.g. NVIDIA, Microsoft, Zomato")

    # EVERYTHING BELOW IS NOW PROPERLY INDENTED INSIDE main()
    if st.button("Generate Intelligence Report"):
        if not company_name:
            st.warning("Please enter a company name.")
            return

        with st.spinner("🕵️ ClientScout is scouring the web..."):
            try:
                report = invoke_agent(company_name)
                
                # Visual Layout
                st.markdown("### 📊 Search Results")
                st.info(f"Analysis for: **{company_name}**")
                
                # Use st.container() with st.markdown directly for best formatting
                with st.container(border=True):
                    st.markdown(report)
                    
            except Exception as e:
                st.error(f"Execution Error: {e}")

    # Sidebar info (Indented inside main)
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