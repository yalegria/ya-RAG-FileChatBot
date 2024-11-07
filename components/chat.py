import streamlit as st
from utils.renders import *
from db.database import log_logout, log_file_upload
from components.footer import add_footer

def show():

    print(st.context.headers)
    for key,value in st.context.headers.items():
        print(f"{key}: {value}")

    # Check if the user is logged in by verifying 'login_id' exists in session state
    if 'login_id' not in st.session_state:
        st.warning("You are not logged in. Please login first.")
        st.stop()  # Stop further execution of the page

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


    
    st.header("EduALizer", divider="red")

    # File uploader
    uploaded_files = st.file_uploader("Please Upload file", type=["png", "jpg", "jpeg", "pdf", "txt", "docx", "doc", "ppt", "pptx", "xls", "xlsx", "csv"], accept_multiple_files=True)
    
    # Detect if files have been uploaded and update session state
    if uploaded_files and uploaded_files != st.session_state.files_uploaded:
        st.session_state.files_uploaded = uploaded_files
        st.session_state.history = []  # Clear chat history
        st.session_state.file_contents = []  # Clear stored file contents
        st.session_state.file_titles = {}  # Clear stored file titles

        for uploaded_file in uploaded_files:
            file_type = uploaded_file.type
            file_name = uploaded_file.name
            file_size = uploaded_file.size

            log_file_upload(st.session_state['login_id'], file_name, file_type, file_size)
        
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

        # Optionally add a logout button
        if st.button("Logout"):
            log_logout(st.session_state['login_id'])  # Log the session duration on logout
            st.session_state['logged_in'] = False
            st.rerun()
        
        
    # Display chat history
    with chat_container:
        st.write("### Conversation History")
        display_history()

        # Textarea within a form for better handling
        with st.form(key='chat_form', clear_on_submit=True):
            query = st.text_area(
                "Ask Edualizer here",
                max_chars=10000, 
                height=100, 
                key="query_input"
            )
            submit_button = st.form_submit_button(label="Send", on_click=send_message)

    add_footer()