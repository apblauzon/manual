import streamlit as st
import plotly.express as px
import pandas as pd
st.set_page_config(page_title="DatViz Ai | Histogram", page_icon="logo.svg")
# Load the dataset
df = pd.read_csv('retail_marketing_2.csv')

def show_histogram():
    st.subheader("Histogram")
    st.markdown("""
    Histograms are useful for visualizing the distribution of a single quantitative variable. They show how often different ranges of values occur, which helps in understanding data distribution and frequency.
    """)


    fig = px.histogram(df, x='Amount', nbins=30, title='Histogram of Sales Amount', labels={'TotalAmount': 'Total Amount'})
    fig.update_layout(annotations=[dict(x=0.99, y=1, xref='paper', yref='paper', xanchor='right', yanchor='bottom', text='Source: DatViz Ai', showarrow=False, font=dict(color='#073DC8'))])
    st.write("")
    st.write("**PROMPT: Generate histogram of Sales Amount.**")
    st.plotly_chart(fig, use_container_width=True)

# Display the histograms
show_histogram()
