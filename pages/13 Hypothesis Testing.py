import streamlit as st
import pandas as pd
import plotly.express as px
import scipy.stats as stats
import numpy as np

st.set_page_config(page_title="DatViz Ai | Hypothesis Testing", page_icon="logo.svg")
df = pd.read_csv('retail_marketing.csv')
df = pd.DataFrame(df)


df = df.dropna(subset=['TotalAmount', 'MarketingPromotion'])


yes_total_amount = df[df['MarketingPromotion'] == 'Yes']['TotalAmount']
no_total_amount = df[df['MarketingPromotion'] == 'No']['TotalAmount']

t_stat, p_value = stats.ttest_ind(yes_total_amount, no_total_amount, equal_var=False)
st.title("Hypothesis Testing")
st.markdown("""A hypothesis test helps evaluate if a sales strategy works by analyzing a small sample of customer interactions to determine if there’s enough evidence to support the claim.""")
st.write("")
st.write("**PROMPT: Test the null hypothesis where Ho: Marketing Promotion does not affect Total Amount of Sales. Show test statistics and graph. What is your conclusion? Use two decimal places only.**")
st.write("")
st.write("")
st.write(f"Test Statistic (t): {t_stat:.2f}")
st.write(f"P-value: {p_value:.2f}")

if p_value < 0.05:
    conclusion = "We reject the null hypothesis. Marketing Promotion affects the Total Amount of Sales."
else:
    conclusion = "We fail to reject the null hypothesis. Marketing Promotion does not significantly affect the Total Amount of Sales."

st.write(conclusion)

fig = px.box(df, x='MarketingPromotion', y='TotalAmount', title='Total Amount by Marketing Promotion')
fig.update_layout(annotations=[dict(x=0.99, y=1, xref='paper', yref='paper', xanchor='right',
                                    yanchor='bottom', text='Source: DatViz Ai', showarrow=False, 
                                    font=dict(color='#073DC8'))])

st.plotly_chart(fig, use_container_width=True)

