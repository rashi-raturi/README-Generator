import streamlit as st
import readme_gen as rg
from dotenv import load_dotenv
import os
load_dotenv()

# function to generate content
def generate(query):
    content = rg.ask(query)

    return content

# Initialize session state for content
if 'content' not in st.session_state:
    st.session_state.content = ""

# Sidebar for selection
with st.sidebar:
    option = st.selectbox('Select:', ['ReadMe', 'LinkedIn Bio'])

# Setting the title based on the selection
if option == 'ReadMe':
    st.title('ReadMe Generator')
    st.divider()

    with st.sidebar:
        project_name = st.text_input('Project Name')
        project_details = st.text_input('Project Details')
        uploaded_files = st.file_uploader('Upload your file', accept_multiple_files=True)
        
        
    if uploaded_files is not None:
        file_data = ''
        for file in uploaded_files:
            file_data += 'Filename: ' + file.name
            file_data += file.read().decode()
            file_data += '\n' 

        query = os.getenv('PROMPT').format(project_name=project_name,file_data=file_data)
    
        # click on the button to generate the response
        if st.sidebar.button('Generate'):
            st.session_state.content = generate(query)
            

        # Toggle between Markdown and Code views
        if st.session_state.content:
            if st.toggle('Preview'):
                st.markdown(st.session_state.content)
            else:
                st.code(st.session_state.content, language='markdown')

                
                
                    

            

                
                            
   
else:
    st.title('LinkedIn Bio Generator')
    with st.sidebar:

        st.button('Generate')
    st.text_area('Enter your LinkedIn bio')


