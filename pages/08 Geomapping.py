import streamlit as st
import plotly.express as px
import pandas as pd

# Load the dataset
df = pd.read_csv('aggregation_data.csv')

def show_geomapping():
    st.header("Geomapping")
    st.markdown("""
    Geomapping is useful for visualizing data spatially on maps. You can use geomaps to see how different metrics are distributed across geographical locations, such as sales or profit by city or region.
    """)

    # Filter data for top 20 highest profit
    st.subheader("Generate geomapping based of number of orders. Group by Marketing Campaign. ")
    df_clean = df.dropna(subset=['Latitude', 'Longitude'])
    grouped_data = df_clean.groupby(['Marketing_Campaign', 'Latitude', 'Longitude'], as_index=False)['Orders'].sum()
    fig = px.scatter_mapbox(grouped_data, lat="Latitude", lon="Longitude", size="Orders", color="Marketing_Campaign", mapbox_style="open-street-map", title="Geographical Distribution of Orders by Marketing Campaign", zoom=12, opacity=0.6)
    fig.update_layout(annotations=[dict(x=0.99, y=1, xref='paper', yref='paper', xanchor='right', yanchor='bottom', text='Source: DatViz Ai', showarrow=False, font=dict(color='#073DC8'))])
    st.plotly_chart(fig, use_container_width=True)

    # st.write("")
    # st.write("")

    # # Filter data for Region = East
    # st.subheader("Generate geomapping based of number of sales.")
    # df_clean = df.dropna(subset=['Latitude', 'Longitude'])
    # fig = px.scatter_mapbox(df_clean, lat='Latitude', lon='Longitude', size='Sales', color='Sales', color_continuous_scale=px.colors.sequential.YlOrBr, zoom=12, mapbox_style='open-street-map', title="Sales Geomap")
    # fig.update_layout(annotations=[dict(x=0.99, y=1, xref='paper', yref='paper', xanchor='right', yanchor='bottom', text='Source: DatViz Ai', showarrow=False, font=dict(color='#073DC8'))])
    # st.plotly_chart(fig, use_container_width=True)


# Display the geomaps
show_geomapping()
