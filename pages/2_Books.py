import streamlit as st
from utils import list_books, upsert_book, remove_book

st.title("📘 Manage Books")

# Show current books
books = list_books()
st.subheader("Current Inventory")
st.dataframe(books)

# Add or update book
st.subheader("Add / Update Book")
with st.form("book_form"):
    bid = st.text_input("Book ID")
    title = st.text_input("Title")
    author = st.text_input("Author")
    total = st.number_input("Total Copies", min_value=1, step=1)
    available = st.number_input("Available Copies", min_value=0, step=1)
    submitted = st.form_submit_button("Save")
    if submitted:
        upsert_book((bid, title, author, total, available))
        st.success("Book saved! Refresh page to see changes.")

# Remove book
st.subheader("Remove Book")
rid = st.text_input("Book ID to remove")
if st.button("Delete Book"):
    remove_book(rid)
    st.success("Book removed! Refresh page to see changes.")
