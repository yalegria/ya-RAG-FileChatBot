import streamlit as st
from utils.renders import *

def show():
    st.markdown("""
        <style>
        .stFormSubmitButton button {
                width: 100% !important;
                background: #4CAF50;
                color: #FFF;
                border-color: #FFF;
            }
        </style>      
    """, unsafe_allow_html=True)


    
    st.header("RAG File Assistant", divider="red")

    # File uploader
    uploaded_files = st.file_uploader("Please Upload file", type=["png", "jpg", "jpeg", "pdf", "txt", "docx", "doc", "ppt", "pptx", "xls", "xlsx", "csv"], accept_multiple_files=True)
    
    # Detect if files have been uploaded and update session state
    if uploaded_files and uploaded_files != st.session_state.files_uploaded:
        st.session_state.files_uploaded = uploaded_files
        st.session_state.history = []  # Clear chat history
        st.session_state.file_contents = []  # Clear stored file contents
        st.session_state.file_titles = {}  # Clear stored file titles
        
        # Assign files to variables and titles
        file_vars = assign_files_to_vars(uploaded_files)


    col1, col2 = st.columns([0.3,0.7])

    with col1:
        input_container = st.container()

    with col2:
        chat_container = st.container()

    with input_container:
        # Display the uploaded files
        if st.session_state.file_titles:
            st.write("### Uploaded Files")
            for file_key, file_title in st.session_state.file_titles.items():
                st.write(f"{file_key}: {file_title}")
        
        
    # Display chat history
    with chat_container:
        st.write("### Conversation History")
        display_history()

        # Textarea


        # Textarea within a form for better handling
        with st.form(key='chat_form', clear_on_submit=True):
            query = st.text_area(
                "Ask your AI Assistant",
                max_chars=10000, 
                height=100, 
                key="query_input"
            )
            submit_button = st.form_submit_button(label="Send", on_click=send_message)
