import streamlit as st
import plotly.express as px
import pandas as pd


# Load the dataset
df = pd.read_csv('aggregation_data.csv')



def show_line_chart():
    st.header("Line Chart")
    st.markdown("""
    Line charts are useful for showing trends over time. You can use them to visualize how metrics such as sales or profit change across different time periods, such as over months, quarters, or years.
    """)

    # Ensure 'Month' is a string and 'Year' is numeric
    df['Month'] = df['Month'].astype(str)
    df['Year'] = pd.to_numeric(df['Year'], errors='coerce')

    # Line Chart of Sales over Month
    st.subheader("Generate Line Chart of Sales over Month.")
    # Create a 'Date' column combining 'Year' and 'Month'
    df['Date'] = pd.to_datetime(df['Year'].astype(str) + '-' + df['Month'] + '-01', format='%Y-%B-%d')
    sales_over_month = df.groupby('Date')['Sales'].sum().reset_index()
    fig_sales = px.line(sales_over_month, x='Date', y='Sales')
    st.plotly_chart(fig_sales)
    st.write("")
    st.write("")
    # Line Chart of Profit by Quarter
    st.subheader("Generate Line Chart of Profit by Quarter.")
    # Create a 'Quarter' column for grouping
    df['Quarter'] = pd.to_datetime(df['Date']).dt.to_period('Q').astype(str)
    profit_by_quarter = df.groupby('Quarter')['Sales'].sum().reset_index()
    fig_profit = px.line(profit_by_quarter, x='Quarter', y='Sales')
    st.plotly_chart(fig_profit)

# Display the charts
show_line_chart()
