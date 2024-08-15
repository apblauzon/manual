import streamlit as st
import plotly.express as px
import pandas as pd

# Load the dataset
df = pd.read_csv('aggregation_data.csv')

def show_bar_chart():
    st.header("Bar Chart")
    st.markdown("""
    Bar charts are useful for comparing quantities across different categories. You can use them to visualize sales, revenue, and other metrics by various segments such as regions or years.
    """)

    # Bar Chart of Sales by Region
    df['Date'] = pd.to_datetime(df['Month'] + ' ' + df['Year'].astype(str), format='%B %Y')
    monthly_sales = df.groupby('Date')['Sales'].sum().reset_index()
    fig = px.bar(monthly_sales, x='Date', y='Sales', title='Monthly Sales from 2022 to 2023', labels={'Sales': 'Sales', 'Date': 'Date'})
    fig.update_layout(xaxis_title='Date', yaxis_title='Sales', xaxis=dict(tickformat="%b %Y"), annotations=[dict(x=0.99, y=1, xref='paper', yref='paper', xanchor='right', yanchor='bottom', text='Source: DatViz Ai', showarrow=False, font=dict(color='#073DC8'))])
    st.plotly_chart(fig, use_container_width=True)
    st.write("")
    st.write("")

    # Bar Chart of Revenue by Year
    st.subheader("Generate bar plot monthly order by chronologically order from 2023 only. ")
    df_2023 = df[df['Year'] == 2023]
    df_2023['Month'] = pd.Categorical(df_2023['Month'], categories=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'], ordered=True)
    monthly_orders = df_2023.groupby('Month')['Orders'].sum().reset_index().sort_values(by='Month')
    fig = px.bar(monthly_orders, x='Month', y='Orders', title='Monthly Orders in 2023', labels={'Orders': 'Number of Orders'}, color='Orders', color_continuous_scale='Viridis')
    fig.update_layout(annotations=[dict(x=0.99, y=1, xref='paper', yref='paper', xanchor='right', yanchor='bottom', text='Source: DatViz Ai', showarrow=False, font=dict(color='#073DC8'))])
    st.plotly_chart(fig, use_container_width=True)


# Display the charts
show_bar_chart()
