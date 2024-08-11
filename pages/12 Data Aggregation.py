import streamlit as st
import pandas as pd

# Load the dataset
df = pd.read_csv('aggregation_data.csv')

def show_aggregations():
    st.header("Data Aggregation")
    st.markdown("""
    Aggregation involves summarizing data by combining multiple records into a single value based on a specified criterion. It helps in analyzing data at different levels, such as by region, month, or year, and is commonly used for reporting and deriving insights from large datasets.
    """)

    # Aggregate Data by sum of Sales every Region
    st.subheader("Aggregate Data by Sum of Sales Every Region.")
    sales_by_region = df.groupby('Region')['Sales'].sum().reset_index()
    st.dataframe(sales_by_region, use_container_width=True)  # Display as table

    # Aggregate Data by count of Orders every Month
    st.subheader("Aggregate Data by Count of Orders Every Month.")
    orders_by_month = df.groupby('Month')['Orders'].count().reset_index()
    st.dataframe(orders_by_month, use_container_width=True)  # Display as table

    # Aggregate Data by total Revenue every Year
    st.subheader("Aggregate Data by Total Revenue Every Year.")
    revenue_by_year = df.groupby('Year')['Revenue'].sum().reset_index()
    st.dataframe(revenue_by_year, use_container_width=True)  # Display as table

# Display the aggregations
show_aggregations()
