import pandas as pd
import numpy as np
import streamlit as st
from scipy import stats
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import plotly.express as px
import statsmodels.api as sm
from scipy.stats import chi2_contingency
import scipy.stats as stats
from scipy.stats import ttest_ind

df = pd.read_csv('retail_marketing.csv')
# Perform the t-test


# Filtering data and dropping missing values in 'Quantity' and 'MarketingPromotion'
df_filtered = df[['Quantity', 'MarketingPromotion']].dropna()

# Separating data based on 'MarketingPromotion'
quantity_yes = df_filtered[df_filtered['MarketingPromotion'] == 'Yes']['Quantity']
quantity_no = df_filtered[df_filtered['MarketingPromotion'] == 'No']['Quantity']

# Performing T-test
t_stat, p_value = ttest_ind(quantity_yes, quantity_no)




# Streamlit app
def show_hypothesis_testing():
    st.title("Hypothesis Testing")
    st.markdown("""
    A hypothesis test helps evaluate if a sales strategy works by analyzing a small sample of customer interactions to determine if there’s enough evidence to support the claim.
    """)
    
    st.write("**T-test on  influence of Marketing Promotion on Quantity of Sales**")
# Displaying the results
    st.write(f'T-statistic: {t_stat}')
    st.write(f'P-value: {p_value}')

    # Drawing conclusion
    if p_value < 0.05:
        st.write("There is a statistically significant influence of Marketing Promotion on the quantity of sales.")
    else:
        st.write("There is no statistically significant influence of Marketing Promotion on the quantity of sales.")

    # Box plot to visualize the influence of Marketing Promotion on Quantity of sales
    fig = px.box(df_filtered, x='MarketingPromotion', y='Quantity', title='Influence of Marketing Promotion on Quantity of Sales')
    fig.update_layout(annotations=[dict(x=0.99, y=1, xref='paper', yref='paper', xanchor='right', yanchor='bottom', text='Source: DatViz Ai', showarrow=False, font=dict(color='#073DC8'))])
    st.plotly_chart(fig, use_container_width=True)

    
# Display the hypothesis testing results
show_hypothesis_testing()

