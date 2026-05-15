import streamlit as st

# =====================================================
# LOGIN PAGE
# =====================================================

def login_page():

    st.title("TransforaIQ Enterprise")

    st.subheader(
        "AI-Native ERP Governance Platform"
    )

    username = st.text_input(
        "Username"
    )

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login"):

        # ==========================================
        # TEMP CLOUD LOGIN FOR DEMO
        # ==========================================

        if (
            username == "admin"
            and
            password == "admin123"
        ):

            st.session_state.logged_in = True

            st.session_state.username = (
                username
            )

            st.session_state.role = "Admin"

            st.success(
                "Login successful"
            )

            st.rerun()

        else:

            st.error(
                "Invalid credentials"
            )