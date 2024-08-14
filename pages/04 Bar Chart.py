import streamlit as st
import plotly.express as px
import pandas as pd

# Load the dataset
df = pd.read_csv('aggregation_data.csv')

def show_bar_chart():
    st.header("Bar Chart")
    st.markdown("""
    Bar charts are useful for comparing quantities across different categories. You can use them to visualize sales, revenue, and other metrics by various segments such as regions or years.
    """)

    # Bar Chart of Sales by Region
    st.subheader("Generate Bar Chart of Sales every Region.")
    sales_by_region = df.groupby('Region')['Sales'].sum().reset_index()
    fig_sales = px.bar(sales_by_region, x='Region', y='Sales')
    st.plotly_chart(fig_sales)

    # Bar Chart of Revenue by Year
    st.subheader("Generate Bar Chart of Revenue every Year.")
    revenue_by_year = df.groupby('Year')['Revenue'].sum().reset_index()
    fig_revenue = px.bar(revenue_by_year, x='Year', y='Revenue')
    st.plotly_chart(fig_revenue)

# Display the charts
show_bar_chart()
