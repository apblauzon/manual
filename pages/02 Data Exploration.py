import streamlit as st

def show_prompting():
    st.header("Data Exploration")
    st.markdown("""
    When prompting, be more precise and specific (e.g., if you want a graph, write "plot" or "chart"; if you want a table, write "table format") to get accurate output.

    **Sample Prompts:**
    - How many rows?
    - How many columns?
    - How many missing values? (Sometimes AI will give you a bar plot, but if you want the response in table form, say "How many missing values in table form?")
    - How many unique values?
    - What are the variables and their data types? (AI does not respond to the prompt "List")
    - How many numeric and categorical variables? List variables.
    - Provide descriptive/summary statistics of all variables.
    - You may also ask DatViz AI for the meaning of some statistical concepts you want to use in your data, e.g., std, mean, max, etc.
    - With DatViz AI, you can do hypothesis testing, e.g., Test the hypothesis that variable X1 is correlated with X2.
    """)

show_prompting()
