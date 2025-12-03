import streamlit as st
import pandas as pd
import plotly.express as px

# Load and clean data
df = pd.read_csv('vehicles_us.csv')
df['model_year'] = df.groupby('model')['model_year'].transform(lambda x: x.fillna(x.median()))
df['cylinders'] = df.groupby('model')['cylinders'].transform(lambda x: x.fillna(x.median()))
df['model_year'] = df['model_year'].fillna(df['model_year'].median()).astype(int)
df['cylinders'] = df['cylinders'].fillna(df['cylinders'].median()).astype(int)
df = df[df['price'] > 100]
df = df[df['price'] <= 100_000]       # Cap at $100k
df = df[df['odometer'] > 0]
df = df[df['odometer'] <= 500_000]    # Cap at 500k miles
df = df[df['model_year'].between(2000, 2025)]

# Streamlit app layout
st.header('Car Advertisement Dashboard (Sprint 4 Project)')

# Checkbox to toggle outlier detail view
show_outliers = st.checkbox('Show Outlier Details (Price > $80k or Mileage > 400k)', value=False)

if show_outliers:
    df_outliers = df[(df['price'] > 80_000) | (df['odometer'] > 400_000)]
    st.subheader('Outlier Analysis')
    st.write(f"Number of outliers: {len(df_outliers):,}")
    st.dataframe(df_outliers[['model', 'price', 'odometer', 'model_year']].head(10))
else:
    st.write("Outliers (price > $80k or mileage > 400k) hidden. Uncheck to explore.")

# Histogram: Price Distribution
st.subheader('Price Distribution (Cars $100–$100k)')
fig1 = px.histogram(df, x='price', nbins=50, title='Price Distribution',
                    labels={'price': 'Price ($)'}, color_discrete_sequence=['#636EFA'])
fig1.update_layout(bargap=0.1, height=400)
st.plotly_chart(fig1)

# Scatter Plot: Price vs Mileage
st.subheader('Price vs Mileage (Interactive)')
fig2 = px.scatter(df, x='odometer', y='price', color='condition',
                  title='Price vs Mileage (Price ≤ $100k, Mileage ≤ 500k miles)',
                  labels={'odometer': 'Mileage (miles)', 'price': 'Price ($)'},
                  hover_data=['model', 'model_year'], opacity=0.6)
fig2.update_layout(height=500)
st.plotly_chart(fig2)