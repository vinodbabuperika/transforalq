import streamlit as st
import pandas as pd

# ---------------------------------------------------
# PAGE HEADER
# ---------------------------------------------------

st.title("AI Gap Analysis Engine")

st.markdown(
    """
AI-powered As-Is vs To-Be transformation assessment
"""
)

# ---------------------------------------------------
# ERP PROCESS SELECTION
# ---------------------------------------------------

st.subheader("Select Transformation Area")

process = st.selectbox(

    "ERP Process",

    [
        "PTP",
        "OTC",
        "RTR"
    ]
)

# ---------------------------------------------------
# AI GAP ANALYSIS
# ---------------------------------------------------

st.subheader("Transformation Gap Analysis")

# ---------------------------------------------------
# PTP
# ---------------------------------------------------

if process == "PTP":

    gap_df = pd.DataFrame({

        "Area": [

            "Invoice Processing",
            "Approval Workflow",
            "PO Matching",
            "Exception Handling",
            "Vendor Queries"

        ],

        "As-Is": [

            "Manual Invoice Entry",
            "Email-Based Approval",
            "Semi-Automated",
            "Manual Resolution",
            "Shared Mailbox"

        ],

        "To-Be": [

            "OCR + AI Extraction",
            "AI Workflow Automation",
            "Touchless Matching",
            "AI Exception Concierge",
            "AI Vendor Portal"

        ],

        "Transformation Impact": [

            "High",
            "High",
            "Medium",
            "High",
            "Medium"

        ]
    })

# ---------------------------------------------------
# OTC
# ---------------------------------------------------

elif process == "OTC":

    gap_df = pd.DataFrame({

        "Area": [

            "Cash Application",
            "Collections",
            "Dispute Resolution",
            "Credit Review",
            "Customer Portal"

        ],

        "As-Is": [

            "Manual Cash Posting",
            "Excel Tracking",
            "Email Follow-up",
            "Spreadsheet Review",
            "No Self-Service"

        ],

        "To-Be": [

            "AI Cash Application",
            "Collections Workflow",
            "AI Dispute Routing",
            "AI Credit Analytics",
            "Digital Customer Portal"

        ],

        "Transformation Impact": [

            "High",
            "Medium",
            "High",
            "Medium",
            "High"

        ]
    })

# ---------------------------------------------------
# RTR
# ---------------------------------------------------

else:

    gap_df = pd.DataFrame({

        "Area": [

            "Journal Entry",
            "Reconciliation",
            "Month-End Close",
            "Variance Analysis",
            "Financial Reporting"

        ],

        "As-Is": [

            "Manual Journal Posting",
            "Excel Reconciliation",
            "Delayed Close",
            "Manual Investigation",
            "Static Reporting"

        ],

        "To-Be": [

            "AI Journal Validation",
            "Auto Reconciliation",
            "Accelerated Close",
            "AI Variance Insights",
            "Real-Time Reporting"

        ],

        "Transformation Impact": [

            "Medium",
            "High",
            "High",
            "Medium",
            "High"

        ]
    })

# ---------------------------------------------------
# SHOW TABLE
# ---------------------------------------------------

st.dataframe(
    gap_df,
    use_container_width=True
)

# ---------------------------------------------------
# AI SUMMARY
# ---------------------------------------------------

st.subheader("AI Executive Assessment")

st.info(f"""

The current {process} landscape shows
significant opportunities for workflow
automation, AI enablement, touchless
processing and SLA governance.

AI recommends phased transformation
using intelligent workflow orchestration
and enterprise automation capabilities.

Expected benefits:

• Reduced manual effort  
• Increased SLA compliance  
• Faster cycle times  
• Reduced operational risk  
• Improved audit controls  
• Enhanced customer/vendor experience

""")

# ---------------------------------------------------
# TRANSFORMATION SCORE
# ---------------------------------------------------

st.subheader("Transformation Opportunity Score")

score = 87

st.progress(score)

st.metric(
    "AI Opportunity Score",
    f"{score}%"
)

# ---------------------------------------------------
# TARGET OPERATING MODEL
# ---------------------------------------------------

st.subheader("AI Target Operating Model")

st.success("""

Target enterprise architecture:

• AI-led workflow orchestration  
• Touchless ERP transaction processing  
• Intelligent exception handling  
• Automated SLA governance  
• Enterprise analytics & KPI visibility  
• Multi-tenant transformation governance

""")

# ---------------------------------------------------
# DOWNLOADABLE OUTPUT
# ---------------------------------------------------

st.subheader("Download Assessment")

csv = gap_df.to_csv(index=False)

st.download_button(

    label="Download Gap Analysis",

    data=csv,

    file_name=f"{process}_gap_analysis.csv",

    mime="text/csv"
)

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------

st.success(
    "AI Gap Analysis Completed Successfully"
)