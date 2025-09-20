import streamlit as st
import pandas as pd
from utils import upsert_book, upsert_student

st.title("🧩 Import from Excel")

uploaded = st.file_uploader("Upload Excel file", type=["xlsx"])

if uploaded:
    xls = pd.ExcelFile(uploaded)
    st.success(f"Uploaded: {uploaded.name}")

    if "Books" in xls.sheet_names:
        books_df = pd.read_excel(xls, "Books")
        st.subheader("Books Preview")
        st.dataframe(books_df.head())
        if st.button("Import Books"):
            for _, row in books_df.iterrows():
                upsert_book((
                    str(row["id"]),
                    str(row["title"]),
                    str(row.get("author", "")),
                    int(row["total_copies"]),
                    int(row["available_copies"]),
                ))
            st.success("Books imported successfully!")

    if "Students" in xls.sheet_names:
        students_df = pd.read_excel(xls, "Students")
        st.subheader("Students Preview")
        st.dataframe(students_df.head())
        if st.button("Import Students"):
            for _, row in students_df.iterrows():
                upsert_student((
                    str(row["id"]),
                    str(row["name"]),
                    str(row.get("email", "")),
                ))
            st.success("Students imported successfully!")
