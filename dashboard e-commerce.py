import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.figure import Figure
from babel.numbers import format_currency

st.title('Dashboard E-Commerce')
st.header('Final Project Luthfi Hakim')


# Read datasets
order_url='https://drive.google.com/file/d/1Mp66lajt3ZJ6iN6o0t9yZlbf2wc-gtUC/view?usp=drive_link'
order_url='https://drive.google.com/uc?id=' + order_url.split('/')[-2]
order_dataset = pd.read_csv(order_url)

product_url='https://drive.google.com/file/d/1THSU_CJGI4Vw0WgrzoX0QfFrq96CrxF6/view?usp=drive_link'
product_url='https://drive.google.com/uc?id=' + product_url.split('/')[-2]
product_dataset = pd.read_csv(product_url)

review_url='https://drive.google.com/file/d/1p1bRB0Ad_oOvzAlPbUGqTQs1uWCSNkv5/view?usp=drive_link'
review_url='https://drive.google.com/uc?id=' + review_url.split('/')[-2]
review_dataset = pd.read_csv(review_url)

items_url='https://drive.google.com/file/d/1_5rzhIyZIlA0sd56JsJg9daoDN-Sylr5/view?usp=drive_link'
items_url='https://drive.google.com/uc?id=' + items_url.split('/')[-2]
items_dataset = pd.read_csv(items_url)

# Merge datasets
merged_df = items_dataset.merge(product_dataset, on='product_id', how='left')
merged_df = merged_df.merge(review_dataset, on='order_id', how='left')
merged_df = merged_df.merge(order_dataset, on='order_id', how='left')

# Drop unnecessary columns
columns_to_drop = ['product_name_lenght', 'product_description_lenght', 'product_photos_qty', 
                   'product_weight_g', 'product_length_cm', 'product_height_cm', 
                   'product_width_cm', 'review_comment_title', 'review_comment_message', 
                   'order_approved_at', 'order_delivered_carrier_date', 
                   'order_delivered_customer_date']
merged_df.drop(columns=columns_to_drop, inplace=True)

with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("data:image/png;base64,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")
    st.markdown(
    """
    # E-Commerce
    Hello, berikut merupakan dashboard simple yang memberikan informasi tentang 5 top barang terlaris beserta rata rata review score dari semua barang!!!
    Dan diakhir terdapat kesimpulan 
    """
)

# Process top 5 categories
top_categories = merged_df['product_category_name'].value_counts().head(5)

# Show top 5 categories
col1, col2 = st.columns([1, 3])
with col1:
    st.subheader('Top 5 Best-Selling Categories')
    st.write(top_categories)

# Show review score distribution
with col2:
    st.subheader('Top 5 Best-Selling Categories')
    top_5_category_sales = merged_df['product_category_name'].value_counts().head(5)
    st.bar_chart(top_5_category_sales)


# Process review score histogram
st.subheader('Average Review Score Seluruh Barang E-Commerce')
fig, ax = plt.subplots(figsize=(8, 6))
ax.hist(merged_df['review_score'], bins=5, edgecolor='black')
ax.axvline(x=merged_df['review_score'].mean(), color='red', linestyle='--', label='Mean Review Score')
ax.set_title('Review Score Distribution')
ax.set_xlabel('Review Score')
ax.set_ylabel('Frequency')
ax.legend()
st.pyplot(fig)



# Mean review score
mean_review_score = merged_df['review_score'].mean()
st.markdown(f"<div style='text-align: center;'>Mean Review Score: {mean_review_score:.2f}</div>", unsafe_allow_html=True)

# Show question 3: correlation between review score and sales
st.subheader('Hubungan Rating Score dan Jumlah Penjualan')

# Filter data untuk kategori barang terlaris
top_5_products = merged_df[merged_df['product_category_name'].isin(top_categories.index)]
correlation = top_5_products.groupby('product_category_name')['review_score'].mean()

# Tampilkan review score untuk top 5 kategori
st.write("Review Score untuk 5 kategori terbaik")
st.write(correlation)

# Filter data untuk kategori lainnya (non top 5)
other_products = merged_df[~merged_df['product_category_name'].isin(top_categories.index)]
correlation_other = other_products.groupby('product_category_name')['review_score'].mean()

# Tampilkan review score untuk kategori lainnya
st.write("Review Score untuk kategori lainnya")
st.write(correlation_other)


st.markdown('''
Berdasarkan hasil yang didapat bahwa ada 3 kategori barang top 5 terlaris yang memiliki average score rating dibawah total kesuluruhan average score rating barang (cama_mesa_banho: 3.90,  informatica_acessorios: 3.93, moveis_decoracao: 3.90, sedangkan seluruh barang average_scorenya 4.032472502046773). Awalnya saya mengira bahwa semakin tinggi rating dari suatu barang, maka barang tersebut akan semakin sering dibeli pelanggan, namun menurut saya berdasarkan hasil tersebut jika rating score tinggi belum tentu tinggi juga jumlah penjualan barangnya.
''')
 
    
