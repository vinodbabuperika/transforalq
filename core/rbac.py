# =========================================
# TRANSFORAIQ RBAC ENGINE
# =========================================

ROLE_PERMISSIONS = {

    "Admin": [
        "Executive Dashboard",
        "Project Plan",
        "RAID Management",
        "RACI Matrix",
        "Stakeholder Governance",
        "Cost & Resource Tracking",
        "Client Master",

        "Statement of Work",
        "Fit-Gap Analysis",
        "Configuration Tracking",
        "Integration Tracking",

        "SIT Planning & Execution",
        "UAT Governance",
        "Defect Tracking",

        "Deployment Tracker",
        "Cutover & Hypercare",

        "Migration Validation",

        "AI PMO Copilot",
        "AI Risk Prediction",
        "AI Mapping Assistant",
        "Agentic Workflow Automation",

        "ERP Discovery",
        "Gap Analysis",
        "AI Recommendations",
        "FDD Generator"
    ],

    "PMO": [
        "Executive Dashboard",
        "Project Plan",
        "RAID Management",
        "RACI Matrix",
        "Stakeholder Governance",

        "ERP Discovery",
        "Gap Analysis",
        "AI Recommendations"
    ],

    "Testing Lead": [
        "SIT Planning & Execution",
        "UAT Governance",
        "Defect Tracking"
    ]
}


def has_access(role, feature):

    permissions = ROLE_PERMISSIONS.get(role, [])

    return feature in permissions