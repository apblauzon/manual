import streamlit as st
import pandas as pd

# Load the dataset
df = pd.read_csv('new_data.csv')
# Convert 'TransactionDate' to datetime format
df['TransactionDate'] = pd.to_datetime(df['TransactionDate'], format='%d/%m/%Y')
df['Month'] = df['TransactionDate'].dt.to_period('M')
monthly_total = df.groupby('Month')['TotalAmount'].sum().reset_index()




def show_aggregations():
    st.header("Data Aggregation")
    st.markdown("""
    Aggregation involves summarizing data by combining multiple records into a single value based on a specified criterion. It helps in analyzing data at different levels, such as by region, month, or year, and is commonly used for reporting and deriving insights from large datasets.
    """)
    st.write("")
    st.write("**PROMPT: Generate a table to display the Total Amount of Sales every month.**")
    # Display the table
    st.dataframe(monthly_total, use_container_width=True)
# Display the aggregations
show_aggregations()
