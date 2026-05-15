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

[data-testid="stAppViewContainer"] {
    background: linear-gradient(
        135deg,
        #f8fbff 0%,
        #eef4ff 100%
    );
}

/* Remove Streamlit top spacing */
.block-container {
    padding-top: 2rem;
    padding-bottom: 1rem;
}

/* Main Login Wrapper */
.login-wrapper {
    display: flex;
    justify-content: center;
    align-items: center;
    padding-top: 30px;
}

/* Main Card */
.login-card {
    display: flex;
    width: 1100px;
    min-height: 700px;
    background: white;
    border-radius: 28px;
    overflow: hidden;
    box-shadow: 0px 10px 40px rgba(0,0,0,0.10);
}

/* Left Panel */
.left-panel {
    width: 48%;
    background: linear-gradient(
        180deg,
        #021b47 0%,
        #0b2c78 100%
    );
    color: white;
    padding: 60px;
}

.logo {
    font-size: 54px;
    font-weight: 700;
    margin-top: 60px;
    line-height: 1.1;
}

.logo-blue {
    color: #4da3ff;
}

.line {
    width: 70px;
    height: 4px;
    background: #4da3ff;
    margin-top: 25px;
    margin-bottom: 35px;
    border-radius: 10px;
}

.tagline {
    font-size: 28px;
    font-weight: 600;
    margin-bottom: 25px;
}

.description {
    font-size: 19px;
    line-height: 1.8;
    color: #dbeafe;
}

/* Right Panel */
.right-panel {
    width: 52%;
    padding: 70px;
    background: white;
}

.welcome {
    font-size: 46px;
    font-weight: 700;
    color: #1e293b;
    margin-top: 40px;
    margin-bottom: 10px;
}

.subtext {
    color: #64748b;
    font-size: 20px;
    margin-bottom: 45px;
}

/* Input fields */
.stTextInput > div > div > input {
    height: 58px;
    border-radius: 14px;
    border: 1px solid #dbe4f0;
    font-size: 18px;
}

/* Login Button */
.stButton > button {
    width: 100%;
    height: 58px;
    border-radius: 14px;
    border: none;
    background: linear-gradient(
        90deg,
        #2563eb 0%,
        #3b82f6 100%
    );
    color: white;
    font-size: 20px;
    font-weight: 600;
    margin-top: 20px;
}

.stButton > button:hover {
    color: white;
    background: linear-gradient(
        90deg,
        #1d4ed8 0%,
        #2563eb 100%
    );
}

/* Footer */
.footer {
    text-align: center;
    margin-top: 25px;
    color: #94a3b8;
    font-size: 15px;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# LOGIN PAGE
# =====================================================

def login_page():

    st.markdown(
        '<div class="login-wrapper">',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="login-card">',
        unsafe_allow_html=True
    )

    # LEFT PANEL
    st.markdown("""
    <div class="left-panel">

        <div class="logo">
            TransforaQ<br>
            <span class="logo-blue">
                Enterprise
            </span>
        </div>

        <div class="line"></div>

        <div class="tagline">
            AI-Native ERP Governance Platform
        </div>

        <div class="description">
            Transform your enterprise operations
            with intelligent automation,
            real-time insights,
            and AI-powered governance.
        </div>

    </div>
    """, unsafe_allow_html=True)

    # RIGHT PANEL
    st.markdown(
        '<div class="right-panel">',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="welcome">Welcome Back</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtext">Please sign in to your account</div>',
        unsafe_allow_html=True
    )

    username = st.text_input(
        "Username",
        placeholder="Enter your username"
    )

    password = st.text_input(
        "Password",
        type="password",
        placeholder="Enter your password"
    )

    if st.button("Login"):

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
        '<div class="footer">© 2026 TransforaIQ Enterprise. All rights reserved.</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )