import streamlit as st
import plotly.express as px
import pandas as pd


# Load the dataset
df = pd.read_csv('new_data.csv')


df['TransactionDate'] = pd.to_datetime(df['TransactionDate'], format='%d/%m/%Y')

# Filter out the years 2025, 2026, 2027
df_filtered = df[~df['TransactionDate'].dt.year.isin([2025, 2026, 2027])]

# Extract year and month from the transaction date for grouping
df_filtered['Month'] = df_filtered['TransactionDate'].dt.to_period('M')

# Calculate the mean total amount by month
monthly_mean = df_filtered.groupby('Month')['TotalAmount'].mean().reset_index()
monthly_mean['Month'] = monthly_mean['Month'].astype(str)



def show_line_chart():
    st.header("Line Chart")
    st.markdown("""
    Line charts are useful for showing trends over time.
    """)

    # Plotly line chart
    fig = px.line(monthly_mean, x='Month', y='TotalAmount', title='Mean Total Amount by Transaction Date in Months (Excluding Years 2025, 2026, 2027)')
    fig.update_layout(xaxis_title='Month', yaxis_title='Mean Total Amount', annotations=[dict(x=0.99, y=1, xref='paper', yref='paper', xanchor='right', yanchor='bottom', text='Source: DatViz Ai', showarrow=False, font=dict(color='#073DC8'))])

    st.plotly_chart(fig, use_container_width=True)

# Display the charts
show_line_chart()
