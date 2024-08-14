import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
# Load the dataset
df = pd.read_csv('aggregation_data.csv')
np.random.seed(42)
df['Discount Percentage'] = np.random.uniform(5, 50, len(df))
df['Profit'] = df['Discount Percentage'] * 1000
df['Quantity Sold'] = np.random.randint(1, 100, len(df))
df['Customer Lifetime Value'] = 10000 / df['Quantity Sold']
df.to_csv('updated_aggregation_data.csv', index=False)



def show_scatterplot():
    st.header("Scatter Plots")
    st.markdown("""
    Scatter plots are useful for visualizing the relationship between two variables. You can use them to see how one metric might influence another.
    """)

    # Scatter Plot: Profit vs Discount Percentage
    st.subheader("Scatter Plot: Profit vs Discount Percentage")
    fig_profit_discount = px.scatter(df, x='Discount Percentage', y='Profit', title='Profit vs Discount Percentage')
    st.plotly_chart(fig_profit_discount)

    # Scatter Plot: Quantity Sold vs Customer Lifetime Value
    st.subheader("Scatter Plot: Quantity Sold vs Customer Lifetime Value")
    fig_qty_clv = px.scatter(df, x='Quantity Sold', y='Customer Lifetime Value', title='Quantity Sold vs Customer Lifetime Value', color_discrete_sequence=['orange'])
    st.plotly_chart(fig_qty_clv)

# Display the scatter plots
show_scatterplot()