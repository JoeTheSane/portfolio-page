import streamlit as st
import pandas


st.set_page_config(layout = "wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/IMG_0951.jpg")

with col2:
    st.title("Joe Madjeski")
    content = """Joe Madjeski has had many jobs in IT: Operations, Support, Change Manager, Server admin, Data Center 
    Management, and more. The newest challenge is software engineering."""
    st.info(content)

content2 = """
Below, you can find some of the apps I have built in Python. Feel free to contact me!
"""

st.write(content2)

csv_dataframe = pandas.read_csv("data.csv", sep=";")

col3, col4 = st.columns(2)


with col3:
    for index, row in csv_dataframe[:10].iterrows():
        st.header(row["title"])


with col4:
    for index, row in csv_dataframe[10:].iterrows():
        st.header(row["title"])