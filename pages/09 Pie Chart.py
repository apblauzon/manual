import streamlit as st
import plotly.express as px
import pandas as pd
st.set_page_config(page_title="DatViz Ai | Pie Chart", page_icon="logo.svg")
# Load the dataset
df = pd.read_csv('new_data.csv')

def show_pie_chart():
    st.subheader("Pie Chart")
    st.markdown("""
    Pie charts are useful for showing the proportion of different categories in a whole. They are ideal for visualizing how different segments contribute to a total, such as quantity by Product ID (category).
    """)

    quantity_distribution = df.groupby('ProductID')['Quantity'].sum().reset_index()

    # Plot a pie chart
    fig = px.pie(quantity_distribution, names='ProductID', values='Quantity', title='Quantity Distribution by Product ID')

    # Add an annotation
    fig.update_layout(annotations=[dict(x=0.99, y=1, xref='paper', yref='paper', xanchor='right', yanchor='bottom', text='Source: DatViz Ai', showarrow=False, font=dict(color='#073DC8'))])

    st.write("")
    st.write("**PROMPT: Generate a pie chart of Quantity by Product ID.**")
    st.plotly_chart(fig, use_container_width=True)
# Display the pie charts
show_pie_chart()
