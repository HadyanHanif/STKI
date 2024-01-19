import streamlit as st
import pandas as pd

# Load dataset
dataset_path = "dataset-ikan.csv"
df = pd.read_csv(dataset_path)

# Print info about columns
st.write("Informasi Kolom dalam Dataset:")
st.write(df.columns)


# Sidebar
st.sidebar.header("Cari Resep Ayam")
search_term = st.sidebar.text_input("Masukkan kata kunci:", "")

# Filter dataset based on search term
filtered_df = df[df['Title'].str.contains(search_term, case=False)]

# Main content
st.title("Aplikasi Pencarian Resep Ikan")
st.write("Temukan resep ayam favorit Anda!")

if len(filtered_df) == 0:
    st.warning("Tidak ada resep yang sesuai dengan kata kunci yang dimasukkan.")
else:
    st.subheader("Resep Ayam yang Cocok:")
    st.table(filtered_df[['Title', 'Ingredients', 'Steps', 'Loves', 'URL']])

# Footer
st.sidebar.markdown("""
    Dibuat oleh [Nama Anda]
    """)