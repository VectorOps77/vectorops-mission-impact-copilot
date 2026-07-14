DOCUMENT_TEMPLATES = {
    "Executive Brief": {
        "description": (
            "Short leadership-focused document with an executive summary, "
            "key points, risks, and next steps."
        ),
        "sections": [
            "Executive Summary",
            "Key Accomplishments",
            "Current Status",
            "Risks / Issues",
            "Recommended Next Steps",
        ],
        "style": "executive",
    },
    "MSR Report": {
        "description": (
            "Monthly status report focused on solutions delivered, "
            "outcomes achieved, risks, and metrics."
        ),
        "sections": [
            "Monthly Summary",
            "Solution Delivered",
            "Outcome Achieved",
            "Customer / Stakeholder Feedback",
            "KPI Updates",
            "Risks / Issues",
            "Next Month Focus",
        ],
        "style": "msr",
    },
    "Technical Report": {
        "description": (
            "Technical documentation format for architecture, "
            "implementation, security, and operations."
        ),
        "sections": [
            "Technical Overview",
            "Architecture",
            "Implementation Details",
            "Security Considerations",
            "Deployment Notes",
            "Operational Support",
            "Future Enhancements",
        ],
        "style": "technical",
    },
    "KPI Report": {
        "description": (
            "Performance measurement format focused on baseline, "
            "target, calculation, and business value."
        ),
        "sections": [
            "KPI Name",
            "Purpose",
            "Baseline",
            "Target",
            "Unit of Measure",
            "Calculation Method",
            "Data Source",
            "Business Value",
        ],
        "style": "kpi",
    },
    "Meeting Summary": {
        "description": (
            "Meeting recap format with decisions, action items, "
            "risks, and follow-ups."
        ),
        "sections": [
            "Meeting Purpose",
            "Summary",
            "Key Decisions",
            "Action Items",
            "Risks / Blockers",
            "Follow-Up Items",
        ],
        "style": "meeting",
    },
    "DevSecOps Report": {
        "description": (
            "DevSecOps project summary covering CI/CD, security scans, "
            "Docker, Azure, and lessons learned."
        ),
        "sections": [
            "Pipeline Overview",
            "CI/CD Workflow",
            "Security Gates",
            "Containerization",
            "Azure Deployment",
            "Secret Management",
            "Lessons Learned",
            "Future Improvements",
        ],
        "style": "devsecops",
    },
}