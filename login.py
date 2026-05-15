import streamlit as st

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="TransforaIQ Enterprise",
    page_icon="🚀",
    layout="wide"
)

# =====================================================
# CUSTOM CSS
# =====================================================

st.markdown("""
<style>

.main {
    background-color: #f5f7fb;
}

.login-container {
    display: flex;
    justify-content: center;
    align-items: center;
    padding-top: 60px;
}

.login-card {
    background: white;
    padding: 50px;
    border-radius: 18px;
    box-shadow: 0px 8px 30px rgba(0,0,0,0.08);
    width: 420px;
}

.title {
    font-size: 42px;
    font-weight: 700;
    color: #1e293b;
    margin-bottom: 5px;
}

.subtitle {
    font-size: 18px;
    color: #64748b;
    margin-bottom: 35px;
}

.stButton > button {
    width: 100%;
    background-color: #2563eb;
    color: white;
    border-radius: 10px;
    height: 48px;
    border: none;
    font-size: 16px;
    font-weight: 600;
}

.stButton > button:hover {
    background-color: #1d4ed8;
    color: white;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# LOGIN PAGE
# =====================================================

def login_page():

    col1, col2, col3 = st.columns([1,2,1])

    with col2:

        st.markdown(
            '<div class="login-container">',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="login-card">',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="title">TransforaIQ Enterprise</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="subtitle">AI-Native ERP Governance Platform</div>',
            unsafe_allow_html=True
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
            # TEMP DEMO LOGIN
            # ==========================================

            if (
                username == "admin"
                and
                password == "admin123"
            ):

                st.session_state.logged_in = True

                st.session_state.username = username

                st.session_state.role = "Admin"

                st.success(
                    "Login successful"
                )

                st.rerun()

            else:

                st.error(
                    "Invalid credentials"
                )

        st.markdown(
            '</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '</div>',
            unsafe_allow_html=True
        )