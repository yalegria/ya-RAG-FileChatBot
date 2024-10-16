import streamlit as st

# Intro page layout (centered header, input, and button)
def show():
    # Custom CSS for vertical and horizontal centering
    st.markdown("""
        <style>
            
            
            .header {
                color: #4CAF50;
                font-size: 40px;
                text-align: center;
            }
            .header span {
                color: #000;
            }
            p {
                text-align: center;
            }
        </style>
    """, unsafe_allow_html=True)

    with st.container():
        st.markdown('<div class="login-box">', unsafe_allow_html=True)
        st.markdown('<div class="header">Edul<span>AI</span>zer</div>', unsafe_allow_html=True)
        st.markdown('<p>This AI buddy helps you analyze your files</p>', unsafe_allow_html=True)
    
        # Input field and button using Streamlit's form
        with st.form("user_id_form", clear_on_submit=True):
            user_id = st.text_input("Enter your ID", "")
            submitted = st.form_submit_button("Continue")

        if submitted:
            if user_id:  # Only proceed if an ID is entered
                st.session_state['logged_in'] = True
                st.rerun() # Force rerun to immediately navigate to chat page
            else:
                st.warning("Please enter a valid ID.")
