import streamlit as st
from utils import init_db

st.set_page_config(page_title="Jigyasa V2 — Library Manager", layout="wide")
st.title("📚 Jigyasa V2 — Library Manager")

st.write("Welcome! Use the navigation below or the sidebar to manage the library.")

# Navigation
st.page_link("pages/1_Import.py", label="🧩 Import from Excel")

st.markdown("---")
st.info("➡️ First time setup? Start with **Import from Excel** to load Books & Students.")

# Initialize DB
init_db()
