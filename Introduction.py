import streamlit as st

st.set_page_config(page_title="DatViz Ai | User Guide", page_icon="logo.svg")
def show_intro():
    # Display the image
    
    st.image("head_logo.svg", use_column_width=True)
    st.header("Users Guide for Prompting")
    st.write("")
    # Display the header and text
    st.markdown("""
    **Welcome to DatViz AI**, a data analytics application powered by OpenAI model ChatGPT4o. Using natural conversation, you can ask DatViz AI to simplify or summarize your data, calculate summary statistics, and generate clear and intuitive visualizations. It can be used in any field requiring quick data analysis and visualization.  DatViz Ai can also be integrated into decision-making and planning processes in business, government, not-for-profit, education and research institutions.
    
    To use DatViz AI effectively, you should be familiar with your data, understand the context in which it was collected, and have some basic understanding of statistics. It is also important to have clear goals for analyzing your data.
    """)

    st.write("")
    st.write("Source of data of this demo: Retail_Transaction_Dataset.csv (from Kaggle) but with mocked-up locations")

show_intro()

