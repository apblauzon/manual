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
    st.subheader("Generate scatterplot by monthly saves versus monthly order. ")
    df['Month_Year'] = df['Month'] + ' ' + df['Year'].astype(str)
    monthly_data = df.groupby('Month_Year').agg({'Sales': 'sum', 'Orders': 'sum'}).reset_index()
    fig = px.scatter(monthly_data, x='Sales', y='Orders', title='Monthly Sales vs Monthly Orders', labels={'Sales': 'Monthly Sales', 'Orders': 'Monthly Orders'}, hover_data=['Month_Year'])
    fig.update_layout(annotations=[dict(x=0.99, y=1, xref='paper', yref='paper', xanchor='right', yanchor='bottom', text='Source: DatViz Ai', showarrow=False, font=dict(color='#073DC8'))])
    st.plotly_chart(fig, use_container_width=True)
    # st.write("")
    # st.write("")

    # # Scatter Plot: Quantity Sold vs Customer Lifetime Value
    # st.subheader("Scatter Plot: Quantity Sold vs Customer Lifetime Value")
    # fig_qty_clv = px.scatter(df, x='Quantity Sold', y='Customer Lifetime Value', title='Quantity Sold vs Customer Lifetime Value', color_discrete_sequence=['orange'])
    # st.plotly_chart(fig_qty_clv)

# Display the scatter plots
show_scatterplot()