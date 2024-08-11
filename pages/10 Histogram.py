import streamlit as st
import plotly.express as px
import pandas as pd

# Load the dataset
df = pd.read_csv('aggregation_data.csv')

def show_histogram():
    st.subheader("Histogram")
    st.markdown("""
    Histograms are useful for visualizing the distribution of a single quantitative variable. They show how often different ranges of values occur, which helps in understanding data distribution and frequency.
    """)

    # Histogram of Sales
    st.subheader("Generate Histogram of Sales.")
    fig_sales_histogram = px.histogram(df, x='Sales',
                                       title='Histogram of Sales',
                                       labels={'Sales': 'Sales Amount'},
                                       nbins=30)  # Number of bins
    st.plotly_chart(fig_sales_histogram)

    # Histogram of Revenue by Year
    st.subheader("Generate Histogram of Revenue by Year.")
    fig_revenue_histogram = px.histogram(df, x='Revenue', color='Year',
                                         title='Histogram of Revenue by Year',
                                         labels={'Revenue': 'Revenue Amount'},
                                         nbins=30)  # Number of bins
    st.plotly_chart(fig_revenue_histogram)

# Display the histograms
show_histogram()
