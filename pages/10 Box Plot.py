import streamlit as st
import plotly.express as px
import pandas as pd

# Load the dataset
df = pd.read_csv('new_data.csv')
df = df.dropna(subset=['Quantity', 'ProductCategory'])

def show_box_plot():
    st.subheader("Box Plot (Box and Whiskers)")
    st.markdown("""
    Box plots are useful for showing the distribution of data and identifying outliers. They are helpful for comparing distributions across different categories, by such as quantity (or sales) by Product ID (or Product Category). 
    """)


    fig = px.box(df, x='ProductCategory', y='Quantity', title="Boxplot of Quantity by Product Category")
    fig.update_layout(annotations=[dict(x=0.99, y=1, xref='paper', yref='paper', xanchor='right', yanchor='bottom', text='Source: DatViz Ai', showarrow=False, font=dict(color='#073DC8'))])

    st.plotly_chart(fig, use_container_width=True)


# Display the box plots
show_box_plot()
