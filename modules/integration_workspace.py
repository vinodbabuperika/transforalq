import streamlit as st

st.title("Integration Workspace")

st.text_area(

    "Integration Details",

    value="""

Interfaces:
- SAP ECC
- OCR Engine
- Workflow API
- Vendor Master Sync
- PO Validation API

Middleware:
- REST APIs
- SAP BAPI
- RFC Connectors

""",

    height=700

)
