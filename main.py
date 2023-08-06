import streamlit as st


st.set_page_config(layout = "wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/IMG_0951.jpg")

with col2:
    st.title("Joe Madjeski")
    content = """Joe Madjeski has had many jobs in IT: Operations, Support, Change Manager, Server admin, Data Center 
    Management, and more. The newest challenge is software engineering."""
    st.info(content)