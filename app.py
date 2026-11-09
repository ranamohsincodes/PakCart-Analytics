import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import sqlite3
import random

st.set_page_config(page_title="PakCart Data Analytics", layout="wide")

# --- STEP A: FAKE DATA GENERATION (Python clean data framework) ---
@st.cache_data
def load_and_clean_data():
    np.random.seed(42)
    cities = ['Karachi', 'Lahore', 'Islamabad', 'Faisalabad', 'Rawalpindi']
    categories = ['Electronics', 'Clothing', 'Groceries', 'Beauty', 'Home Decor']
    statuses = ['Delivered', 'Cancelled', 'Returned']
    
    data = []
    for i in range(1000):
        city = random.choice(cities)
        cat = random.choice(categories)
        status = np.random.choice(statuses, p=[0.75, 0.15, 0.10])
        price = random.randint(150, 5000) if cat != 'Electronics' else random.randint(5000, 50000)
        qty = random.randint(1, 4)
        
        # Delivery days calculation
        delivery_days = random.randint(1, 7) if status == 'Delivered' else None
        
        data.append({
            'Order_ID': f'PK-{100000 + i}',
            'City': city,
            'Category': cat,
            'Price_PKR': price,
            'Quantity': qty,
            'Total_Amount_PKR': price * qty,
            'Status': status,
            'Delivery_Time_Days': delivery_days
        })
    
    df = pd.DataFrame(data)
    
    # Cleaning missing values for analyst representation
    df['Delivery_Time_Days'] = df['Delivery_Time_Days'].fillna(-1) 
    return df

df = load_and_clean_data()

# --- STEP B: SQL DATABASE SYSTEM (Recruiter ko SQL skills dikhane ke liye) ---
conn = sqlite3.connect('pakcart.db')
df.to_sql('orders', conn, if_exists='replace', index=False)

# --- STEP C: DASHBOARD INTERFACE (Streamlit Web App) ---
st.title("📦 PakCart E-Commerce Analytics Dashboard")
st.markdown("#### Real-Time Business Intelligence & Supply Chain Insights")
st.markdown("---")

# 1. Top Level Metrics (KPIs)
total_sales = pd.read_sql("SELECT SUM(Total_Amount_PKR) FROM orders WHERE Status = 'Delivered'", conn).iloc[0,0]
total_orders = pd.read_sql("SELECT COUNT(Order_ID) FROM orders", conn).iloc[0,0]
cancel_rate = pd.read_sql("SELECT (COUNT(*)*100.0 / (SELECT COUNT(*) FROM orders)) FROM orders WHERE Status = 'Cancelled'", conn).iloc[0,0]

kpi1, kpi2, kpi3 = st.columns(3)
kpi1.metric(label="Total Revenue (Delivered Orders)", value=f"Rs. {total_sales:,}")
kpi2.metric(label="Total Orders Placed", value=f"{total_orders:,}")
kpi3.metric(label="Order Cancellation Rate", value=f"{cancel_rate:.2f}%")

st.markdown("---")

# 2. Graphs Section
col1, col2 = st.columns(2)

with col1:
    st.subheader("🏙️ Revenue Breakdown by City")
    city_query = "SELECT City, SUM(Total_Amount_PKR) as Revenue FROM orders WHERE Status = 'Delivered' GROUP BY City ORDER BY Revenue DESC"
    city_df = pd.read_sql(city_query, conn)
    fig_city = px.bar(city_df, x='City', y='Revenue', color='City', labels={'Revenue':'Revenue (PKR)'})
    st.plotly_chart(fig_city, use_container_width=True)

with col2:
    st.subheader("🛍️ Product Categories Distribution")
    cat_query = "SELECT Category, COUNT(Order_ID) as Total_Orders FROM orders GROUP BY Category"
    cat_df = pd.read_sql(cat_query, conn)
    fig_pie = px.pie(cat_df, values='Total_Orders', names='Category', hole=0.4)
    st.plotly_chart(fig_pie, use_container_width=True)

# 3. Raw Data Search Table
st.subheader("🔍 Deep-Dive Data Explorer")
city_filter = st.selectbox("Filter by City", ['All'] + list(df['City'].unique()))

if city_filter != 'All':
    filtered_df = pd.read_sql(f"SELECT * FROM orders WHERE City = '{city_filter}'", conn)
else:
    filtered_df = pd.read_sql("SELECT * FROM orders", conn)

st.dataframe(filtered_df, use_container_width=True)
conn.close()
