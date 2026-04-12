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

    # Inside app.py, replace the report display area:
if st.button("Generate Intelligence Report"):
    with st.spinner("🕵️ ClientScout is scouring the web..."):
        report = invoke_agent(company_name)
        
        # Create a visually distinct card for the report
        with st.container():
            st.markdown("### 📊 Search Results")
            st.info(f"Analysis for: **{company_name}**")
            
            # This puts the report inside a clean box
            st.markdown(f"""
            <div style="border:1px solid #e6e9ef; padding: 20px; border-radius: 10px; background-color: #f9f9f9; color: #31333f;">
                {report}
            </div>
            """, unsafe_allow_html=True)

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