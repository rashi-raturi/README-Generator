import streamlit as st

def sidebarView():
    with st.sidebar:
        st.button('Generate')


def mainView():
    st.title('LinkedIn Bio Generator')
    
    st.text_area('Enter your LinkedIn bio')