import streamlit as st
import plotly.express as px
import pandas as pd

# Load the dataset
df = pd.read_csv('aggregation_data.csv')

def show_scatter_plot():
    st.header("Scatter Plot")
    st.markdown("""
    Scatter plots are useful for visualizing the relationship between two quantitative variables. You can use them to analyze correlations, distributions, and patterns between different metrics.
    """)

    # Ensure 'Profit' and 'Cost' columns are numeric
    df['Sales'] = pd.to_numeric(df['Sales'], errors='coerce')
    df['Orders'] = pd.to_numeric(df['Orders'], errors='coerce')

    # Scatter Plot of Revenue vs. Cost
    st.subheader("Generate Scatter Plot of Profit versus Sales.")
    scatter_revenue_cost = px.scatter(df, x='Sales', y='Orders', title="Sales vs Orders")
    st.plotly_chart(scatter_revenue_cost)

    # Scatter Plot of Profit vs. Sales
    st.subheader("Generate Scatter Plot of Revenue vs Sales.")
    scatter_profit_sales = px.scatter(df, x='Revenue', y='Sales', title="Revenue vs Sales")
    st.plotly_chart(scatter_profit_sales)

# Display the scatter plots
show_scatter_plot()
