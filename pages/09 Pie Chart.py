import streamlit as st
import plotly.express as px
import pandas as pd

# Load the dataset
df = pd.read_csv('aggregation_data.csv')

def show_pie_chart():
    st.subheader("Pie Chart")
    st.markdown("""
    Pie charts are useful for showing the proportion of different categories in a whole. They are ideal for visualizing how different segments contribute to a total, such as quantity or profit distribution.
    """)

    # Pie Chart of Sales by Region
    st.subheader("Generate Pie Chart of Sales by Region.")
    sales_by_region = df.groupby('Region')['Sales'].sum().reset_index()
    fig_sales_region = px.pie(sales_by_region, names='Region', values='Sales', 
                             title='Sales Distribution by Region',
                             color_discrete_sequence=px.colors.sequential.Plasma)
    st.plotly_chart(fig_sales_region)
    
    st.write("")
    st.write("")



    # Pie Chart of Profit by Region
    st.subheader("Generate Pie Chart of Profit by Region.")
    profit_by_region = df.groupby('Region')['Revenue'].sum().reset_index()  # Assuming 'Revenue' represents profit
    fig_profit = px.pie(profit_by_region, names='Region', values='Revenue', 
                        title='Profit Distribution by Region',
                        labels={'Revenue': 'Total Profit'},
                        color_discrete_sequence=['blue', 'lightblue', 'lightyellow', 'yellow'])  # Custom blue to yellow color palette
    st.plotly_chart(fig_profit)

# Display the pie charts
show_pie_chart()
