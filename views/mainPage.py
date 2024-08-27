import streamlit as st

def sidebarView():
    with st.sidebar:
        option = st.selectbox('Select:', ['ReadMe', 'LinkedIn Bio'])

    return option