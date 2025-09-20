import streamlit as st
from utils import list_students, upsert_student, remove_student

st.title("🧑‍🎓 Manage Students")

# Show current students
students = list_students()
st.subheader("Current Students")
st.dataframe(students)

# Add or update student
st.subheader("Add / Update Student")
with st.form("student_form"):
    sid = st.text_input("Student ID")
    name = st.text_input("Name")
    email = st.text_input("Email")
    submitted = st.form_submit_button("Save")
    if submitted:
        upsert_student((sid, name, email))
        st.success("Student saved! Refresh page to see changes.")

# Remove student
st.subheader("Remove Student")
rid = st.text_input("Student ID to remove")
if st.button("Delete Student"):
    remove_student(rid)
    st.success("Student removed! Refresh page to see changes.")
