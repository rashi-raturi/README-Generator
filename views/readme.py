import streamlit as st
from dotenv import load_dotenv
import os
import controllers.readme_gen as rg
from streamlit_extras.mention import mention
from streamlit_extras.bottom_container import bottom

load_dotenv()


def sidebarView():
    
    st.title('ReadMe Generator')
    st.divider()

    with st.sidebar:
        project_name = st.text_input('Project Name')

        project_details = st.text_area('Project Details')
        st.markdown("<p align= 'center' > OR </p> ", unsafe_allow_html=True)
        uploaded_files = st.file_uploader('Upload your file', accept_multiple_files=True)

    return project_name, project_details, uploaded_files

def getFileData(uploaded_files):
    file_data = ''
    for file in uploaded_files:
        file_data += 'Filename: ' + file.name
        file_data += file.read().decode()
        file_data += '\n'

    return file_data

def mainView():

    project_name, project_details, uploaded_files = sidebarView()
         
    if uploaded_files is not None:
        file_data = getFileData(uploaded_files) 

        query = os.getenv('PROMPT').format(project_name=project_name,file_data=file_data)
    
        st.sidebar.divider()
        # click on the button to generate the response
        if st.sidebar.button('Generate'):
            st.session_state.content = rg.ask(query)

        
            
        # Toggling between Markdown and Code views
        if st.session_state.content:
            if st.toggle('Preview'):
                st.markdown(st.session_state.content)
            else:
                st.code(st.session_state.content, language='markdown')
    
    else:
        query = os.getenv('PROMPT').format(project_name=project_name,file_data=project_details)

        # click on the button to generate the response
        if st.sidebar.button('Generate'):
            st.session_state.content = rg.ask(query)
            
        # Toggling between Markdown and Code views
        if st.session_state.content:
            if st.toggle('Preview'):
                st.markdown(st.session_state.content)
            else:
                st.code(st.session_state.content, language='markdown')





        

    