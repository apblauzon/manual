import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(page_title="DatViz Ai | Line Chart", page_icon="logo.svg")
# Load the dataset
df = pd.read_csv('retail_marketing_2.csv')


df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y', errors='coerce')

# Filter out the years 2025, 2026, 2027
df_filtered = df[~df['Date'].dt.year.isin([2025, 2026, 2027])]

# Extract year and month from the transaction date for grouping
df_filtered['Month'] = df_filtered['Date'].dt.to_period('M')

# Calculate the mean total amount by month
monthly_mean = df_filtered.groupby('Month')['Amount'].mean().reset_index()
monthly_mean['Month'] = monthly_mean['Month'].astype(str)



def show_line_chart():
    st.header("Line Chart")
    st.markdown("""
    Line charts are useful for showing trends over time.
    """)

    # Plotly line chart
    fig = px.line(monthly_mean, x='Month', y='Amount', title='Mean Total Amount by Date in Months. ')
    fig.update_layout(xaxis_title='Month', yaxis_title='Mean Total Amount', annotations=[dict(x=0.99, y=1, xref='paper', yref='paper', xanchor='right', yanchor='bottom', text='Source: DatViz Ai', showarrow=False, font=dict(color='#073DC8'))])

    st.write("")
    st.write("**PROMPT: Generate a line chart of Mean Total Amount by Date in months.**")
    st.plotly_chart(fig, use_container_width=True)

# Display the charts
show_line_chart()
