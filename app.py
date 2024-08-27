import streamlit as st
import views.readme as rv

st.set_page_config(page_title="ReadMe Generator")

# Session state for content -> helps in toggling preview (code/markdown)
if 'content' not in st.session_state:
    st.session_state.content = ""

# Main View
rv.mainView()




