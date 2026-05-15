# =====================================================
# FALLBACK AI SERVICE
# =====================================================

def generate_document(prompt):

    if "Functional Design Document" in prompt:

        return """

# Functional Design Document (FDD)

## 1. Business Overview
AI-driven SAP AP automation implementation.

## 2. Scope
- Invoice ingestion
- Validation workflows
- Approval routing
- ERP integration

## 3. Company Codes
- 1000
- 2000
- 3000

## 4. Invoice Sources
- Email
- Vendor Portal
- OCR Upload

## 5. Validation Rules
- Duplicate invoice check
- PO validation
- Vendor validation

## 6. Interfaces
- SAP ECC
- OCR Engine
- Workflow Engine

## 7. Workflow Design
- AP Processor
- AP Manager
- Finance Controller

## 8. Notifications
- Approval alerts
- Exception alerts
- SLA escalation

## 9. Assumptions
- SAP connectivity available
- OCR enabled

## 10. Risks
- ERP downtime
- Master data inconsistency

"""

    elif "Technical Design Document" in prompt:

        return """

# Technical Design Document (TDD)

## 1. Architecture
Cloud-native AP automation platform.

## 2. Components
- OCR Service
- AI Classification
- Workflow Engine
- SAP Connector

## 3. APIs
- SAP BAPI
- REST APIs
- Authentication APIs

## 4. Security
- SSO
- RBAC
- Encryption

## 5. Deployment
- Kubernetes
- Azure Cloud
- CI/CD pipeline

## 6. Monitoring
- Application Insights
- Logging
- Audit Trail

"""

    else:

        return """

# Configuration Workbook

## Workflow Configuration
- Approval matrix
- Escalation rules
- SLA setup

## ERP Mapping
- Vendor master mapping
- Company code mapping
- GL mapping

## Notification Setup
- Email alerts
- Workflow notifications

## User Groups
- AP Clerk
- AP Manager
- Finance Controller

"""