import streamlit as st
import pandas as pd
df = pd.read_csv('new_data.csv')
df2 = pd.read_csv('retail_marketing.csv')

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
    - How many numeric and categorical variables?
    - Provide descriptive/summary statistics of all variables.
    - You may also ask DatViz AI for the meaning of some statistical concepts you want to use in your data, e.g., std, mean, max, etc.
    - With DatViz AI, you can do hypothesis testing, e.g., Test the hypothesis that variable X1 is correlated with X2.
    """)

    type_mapping = df.dtypes.astype(str).map(lambda x: 'Numerical' if x in ['int64', 'float64'] else 'Character')
    missing_values = df.isna().sum()

    # Combine type information and missing values into a DataFrame
    info_df = pd.DataFrame({'Data Type': type_mapping, 'Missing Values': missing_values}).reset_index()
    info_df.columns = ['Variable', 'Data Type', 'Missing Values']
    
    st.write("")
    st.write("**PROMPT: Generate a table to display the variables with their data types and number of missing values.**")
    # Display the DataFrame in Streamlit
    st.dataframe(info_df, use_container_width=True)
    
    st.write("")
    st.write("**PROMPT: Generate a table to display the descriptive statistics of Quantity, Price, Discount Applied and Total Amount.**")
    summary_stats = df2.iloc[:, 3:].describe()
    st.dataframe(summary_stats, use_container_width=True)

show_prompting()
