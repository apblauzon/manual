import streamlit as st

def show_intro():
    # Display the image
    st.image("head_logo.svg", use_column_width=True)

    # Display the header and text
    st.header("Introduction")
    st.markdown("""
    **Welcome to DatViz AI**, a data analytics application powered by OpenAI model ChatGPT4o. Using natural conversation, you can ask DatViz AI to simplify or summarize your data, calculate summary statistics, and generate clear and intuitive visualizations. It can be used in any field requiring quick data analysis and visualization.
    
    **Note**: To use DatViz AI effectively, you should be familiar with your data, understand the context in which it was collected, and have some basic understanding of statistics. It is also important to have clear golas for analyzing your data.
    """)

show_intro()
