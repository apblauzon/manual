import streamlit as st
import plotly.express as px
import pandas as pd

# Load the dataset
df = pd.read_csv('aggregation_data.csv')

def show_box_plot():
    st.subheader("Box Plot (Box and Whiskers)")
    st.markdown("""
    Box plots are useful for showing the distribution of data and identifying outliers. They are helpful for comparing distributions across different categories, such as sales or revenue by region or month.
    """)

    # Box Plot of Sales by Region
    st.subheader("Generate Box Plot of Sales by Region.")
    fig_sales_region = px.box(df, x='Region', y='Sales',
                              title='Box Plot of Sales by Region',
                              labels={'Sales': 'Sales Amount'})
    st.plotly_chart(fig_sales_region)

    # Box Plot of Revenue by Month
    st.subheader("Generate Box Plot of Revenue by Month.")
    fig_revenue_month = px.box(df, x='Month', y='Revenue',
                               title='Box Plot of Revenue by Month',
                               labels={'Revenue': 'Revenue Amount'})
    st.plotly_chart(fig_revenue_month)

# Display the box plots
show_box_plot()
