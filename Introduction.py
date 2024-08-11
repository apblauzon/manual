import streamlit as st

def show_intro():
    # Display the image
    st.image("head_logo.svg", use_column_width=True)

    # Display the header and text
    st.header("Introduction")
    st.markdown("""
    **Welcome to DatViz AI**, a data analytics application powered by OpenAI model ChatGPT4o. Using natural conversation, you can ask DatViz AI to simplify or summarize your data, calculate summary statistics, and generate clear and intuitive visualizations. DatViz AI is a must-have for businesses, not-for-profit organizations, and government institutions. It can be used in any field requiring quick data analysis and visualization.
    
    **Note**: To use DatViz AI effectively, you should be familiar with your data, understand the context in which it was collected, and have clear goals for analyzing your data. A basic understanding of statistics is also helpful.
    """)

show_intro()
