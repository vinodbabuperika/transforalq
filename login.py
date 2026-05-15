import streamlit as st

# =====================================================
# AUTO LOGIN FOR CLOUD DEMO
# =====================================================

def login_page():

    st.session_state.logged_in = True

    st.session_state.username = "admin"

    st.session_state.role = "Admin"

    st.success(
        "Demo login enabled"
    )

    st.rerun()