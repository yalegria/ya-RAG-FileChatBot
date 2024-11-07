# footer.py

import streamlit as st

def add_footer():
    st.markdown(
        """
        <style>
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: #f1f1f1;
            text-align: center;
            padding: 10px 0;
            color: #333;
        }
        .footer a {
            color: #333;
            text-decoration: none;
            font-weight: bold;
        }
        </style>

        <div class="footer">
            <p>Report a <a href="https://grid.rutgers.edu/edualizer-bug" target="_blank">Bug</a> | 
            Provide <a href="https://grid.rutgers.edu/edualizer-feedback" target="_blank">Feedback</a></p>
            <p><small>Y. Alegria - Rutgers</small></p>
        </div>
        """, 
        unsafe_allow_html=True
    )
