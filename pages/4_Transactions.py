import streamlit as st
from utils import search_books, search_students, lend_book, return_book, list_transactions

st.title("🔁 Transactions")

# Issue a Book
st.subheader("Issue a Book")
q_book = st.text_input("Search Book Title")
books = search_books(q_book, require_available=True) if q_book else []
book_choice = None
if books:
    book_choice = st.selectbox("Select Book", books, format_func=lambda x: f"{x[1]} ({x[4]} available)")

q_student = st.text_input("Search Student Name")
students = search_students(q_student) if q_student else []
student_choice = None
if students:
    student_choice = st.selectbox("Select Student", students, format_func=lambda x: f"{x[1]} ({x[0]})")

if st.button("Lend Book"):
    if book_choice and student_choice:
        ok, msg = lend_book(student_choice[0], book_choice[0])
        if ok:
            st.success(f"Issued until {msg}")
        else:
            st.error(msg)

st.markdown("---")
st.subheader("Transaction Log")

# Transaction log
txs = list_transactions()
for tx in txs:
    returned = bool(tx[7])
    style = "color:gray;" if returned else ""
    st.markdown(f"<div style='{style}'>"
                f"{tx[2]} borrowed '{tx[4]}' on {tx[5]}, due {tx[6]}"
                f"</div>", unsafe_allow_html=True)
    if not returned:
        if st.button("Mark Returned", key=f"ret_{tx[0]}"):
            ok, msg = return_book(tx[0])
            if ok:
                st.success("Book returned! Refresh page to see changes.")
            else:
                st.error(msg)
