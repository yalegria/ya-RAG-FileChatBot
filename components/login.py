import streamlit as st
from db.database import log_login
from utils.network_utils import get_ip, get_browser_info, parse_user_agent
from components.footer import add_footer

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
        st.markdown('<p>I am here to help you analyze your files.</p>', unsafe_allow_html=True)
    
        # Input field and button using Streamlit's form
        with st.form("user_id_form", clear_on_submit=True):
            user_id = st.text_input("Enter your netid", "")
            submitted = st.form_submit_button("Continue")

        if submitted:
            if user_id:  # Only proceed if an ID is entered
                st.session_state['logged_in'] = True
                st.session_state['user_id'] = user_id

                # Gather IP, browser, and user agent info
                ip_address = get_ip()  # Fetch IP
                user_agent = get_browser_info()  # Fetch Browser Info


                if user_agent != "Unavailable":
                    try:
                        browser, device, device_type = parse_user_agent(user_agent)  # Parse user agent details
                    except Exception as e:
                        st.error(f"Error parsing user agent: {e}")
                        browser, device, device_type = "Unknown", "Unknown", "Unknown"
                else:
                    st.error("User agent is unavailable.")
                    browser, device, device_type = "Unknown", "Unknown", "Unknown"

                # Log login activity in PostgreSQL with user info
                st.session_state['login_id'] = log_login(user_id, ip_address, user_agent, browser, device)

                st.rerun() # Force rerun to immediately navigate to chat page
            else:
                st.warning("Please enter a valid netid.")

    add_footer()