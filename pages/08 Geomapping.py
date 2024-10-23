import streamlit as st
import plotly.express as px
import pandas as pd
st.set_page_config(page_title="DatViz Ai | Geomapping", page_icon="logo.svg")
# Load the dataset
df = pd.read_csv('new_data.csv')

# Clean data and rename Address to City
df_clean = df.dropna(subset=['lon', 'lat']).rename(columns={"Address": "City"})

def show_geomapping():
    st.header("Geomapping")
    st.markdown("""
    Geomapping is useful for visualizing data spatially on maps. You can use geomaps to see how different metrics are distributed across geographical locations.
    """)

    # Plotly scatter mapbox
    fig = px.scatter_mapbox(df_clean, lat="lat", lon="lon", hover_name="City", hover_data=["ProductCategory", "TotalAmount"],
                            color="TotalAmount", size="TotalAmount", zoom=12, height=600, opacity=0.7,
                            title="Geomapping of Transactions Centered at Manila")

    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(mapbox_center={"lat": 14.599512, "lon": 120.984222})

    fig.update_layout(annotations=[dict(x=0.99, y=1, xref='paper', yref='paper', xanchor='right', yanchor='bottom',
                                        text='Source: DatViz Ai', showarrow=False, font=dict(color='#073DC8'))])

    st.write("")
    st.write("**PROMPT: Generate geomapping based on totalAmount.**")
    st.plotly_chart(fig, use_container_width=True)

# Display the geomaps
show_geomapping()
