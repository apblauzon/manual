import streamlit as st
import plotly.express as px
import pandas as pd

# Load the dataset
df = pd.read_csv('new_data.csv')

def show_bar_chart():
    st.header("Bar Chart")
    st.markdown("""
    Bar charts are useful for comparing quantities across different categories.
    """)

    # Bar Chart of Sales by Region
    total_quantity = df.groupby('ProductID')['Quantity'].sum().reset_index()

    fig = px.bar(total_quantity, x='ProductID', y='Quantity', color='ProductID', 
                title='Total Quantity by Product ID', labels={'Quantity': 'Total Quantity'},
                color_discrete_sequence=px.colors.qualitative.Pastel)

    fig.update_layout(annotations=[dict(x=0.99, y=1, xref='paper', yref='paper', xanchor='right', yanchor='bottom', text='Source: DatViz Ai', showarrow=False, font=dict(color='#073DC8'))])
    st.write("")
    st.write("**PROMPT: Generate a bar chart using ProductID and Quantity.**")
    st.plotly_chart(fig, use_container_width=True)

# Display the charts
show_bar_chart()
