import os
import streamlit as st

from components import login, chat

# Initialize session state attributes
if 'history' not in st.session_state:
    st.session_state.history = []
if 'files_uploaded' not in st.session_state:
    st.session_state.files_uploaded = []
if 'file_contents' not in st.session_state:
    st.session_state.file_contents = []  # Store extracted text content from files
if 'file_titles' not in st.session_state:
    st.session_state.file_titles = {}  # Store file titles

# Title
st.set_page_config(
    page_title="RAG File Assistant - Yuri Alegria",
    page_icon=":robot:",  # You can use emoji or the path to an image file
)

hide_streamlit_style = """
        <style>
            #MainMenu {visibility: hidden;}
            header {visibility: hidden;}
        </style>
    """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

####################
### MAIN HANDLER ###
####################

if 'query_input' not in st.session_state:
    st.session_state.query_input = ""

# Initialize session state for login
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

# Logic to switch between pages
if st.session_state['logged_in']:
    chat.show()
else:
    login.show()


