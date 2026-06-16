import os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4.1-mini")

client = OpenAI(api_key=OPENAI_API_KEY)

st.set_page_config(
    page_title="VectorOps Mission Impact Copilot",
    page_icon="📊",
    layout="wide"
)

st.title("📊 VectorOps Mission Impact Copilot")
st.write(
    "Turn raw project updates into outcome-based stories, KPIs, "
    "monthly updates, and leadership-ready MSR content."
)

st.warning(
    "AI-generated content must be reviewed by a human before being used in any official report."
)

def ask_openai(prompt: str) -> str:
    """
    Sends the prompt to OpenAI and returns the model response.
    """

    if not OPENAI_API_KEY:
        return "Error: OPENAI_API_KEY is missing. Add it to your .env file."

    response = client.responses.create(
        model=MODEL_NAME,
        instructions=(
            "You are a senior Technical Program Manager, DevSecOps advisor, "
            "and project reporting specialist. You help convert raw project activity "
            "into outcome-focused, measurable, executive-ready reporting. "
            "Do not invent facts, metrics, or customer feedback. "
            "If information is missing, clearly state what is missing."
        ),
        input=prompt
    )

    return response.output_text


tab1, tab2, tab3, tab4 = st.tabs(
    [
        "Story Assistant",
        "KPI Builder",
        "Monthly Update Assistant",
        "Quality Checker"
    ]
)


with tab1:
    st.header("Story Creation Assistant")

    story_input = st.text_area(
        "Enter raw project idea or problem statement",
        height=220,
        placeholder=(
            "Example: Reporting is manual, updates are inconsistent, "
            "leadership does not have clear visibility into project health..."
        )
    )

    if st.button("Generate Story", key="story_button"):
        if not story_input.strip():
            st.warning("Enter a project idea first.")
        else:
            prompt = f"""
Create an outcome-based project story from the following input:

{story_input}

Return the response in this exact format:

## Story Title
A clear title for the project story.

## Problem Statement
Describe the client or mission problem being solved.

## Intended Outcome
Describe what success looks like and what improves.

## Suggested KPIs
List 3 measurable KPIs that align to the problem and intended outcome.

## Quality Notes
Explain whether the story is outcome-focused and leadership-ready.

Rules:
- Focus on mission impact.
- Avoid vague task-only language.
- Do not invent specific metrics unless clearly labeled as assumptions.
- Make the language professional and executive-ready.
"""
            with st.spinner("Generating story..."):
                result = ask_openai(prompt)
                st.markdown(result)


with tab2:
    st.header("KPI Builder")

    kpi_input = st.text_area(
        "Enter KPI idea",
        height=220,
        placeholder=(
            "Example: Reduce time spent creating monthly reports "
            "by automating project update summaries..."
        )
    )

    if st.button("Generate KPI", key="kpi_button"):
        if not kpi_input.strip():
            st.warning("Enter a KPI idea first.")
        else:
            prompt = f"""
Build a measurable KPI from this idea:

{kpi_input}

Return the response in this exact format:

## KPI Name
## Reference
Examples: User Time Saved, Cost Avoidance, Accuracy, Customer Satisfaction, Rework Rate

## Baseline
Current state before improvement.

## Basis of Estimate
Where the baseline came from.

## Target
Desired future state.

## Unit of Measure
Examples: hours, dollars, percent, count.

## Calculation
Formula or method for calculating the KPI.

## How This Helps the Client
Explain the business or mission value.

Rules:
- KPI must be measurable.
- KPI must connect to a clear problem.
- Do not invent hard numbers unless clearly labeled as assumptions.
"""
            with st.spinner("Building KPI..."):
                result = ask_openai(prompt)
                st.markdown(result)


with tab3:
    st.header("Monthly Update Assistant")

    update_input = st.text_area(
        "Paste raw monthly update notes",
        height=260,
        placeholder=(
            "Example: Built Power BI report, fixed data refresh issue, "
            "met with stakeholders, improved weekly visibility..."
        )
    )

    if st.button("Generate Monthly Update", key="monthly_button"):
        if not update_input.strip():
            st.warning("Enter monthly update notes first.")
        else:
            prompt = f"""
Convert these raw monthly notes into a professional MSR-style update:

{update_input}

Return the response in this exact format:

## Solution Delivered
What work was completed this month?

## Outcome Achieved
What changed, improved, or moved forward because of the work?

## Customer Feedback
Only include feedback if it was provided. Otherwise say: Not provided.

## Risks / Issues
List risks, issues, or blockers.

## Action Items
Create a table with: Action Item | Owner | Due Date

## Suggested KPI Updates
Recommend measurable values that should be tracked.

Rules:
- Use outcome-focused language.
- Do not exaggerate.
- Do not invent customer feedback.
- If data is missing, recommend what should be tracked.
"""
            with st.spinner("Generating monthly update..."):
                result = ask_openai(prompt)
                st.markdown(result)


with tab4:
    st.header("Quality & Alignment Checker")

    quality_input = st.text_area(
        "Paste story, KPI, or MSR content to review",
        height=260,
        placeholder="Paste generated or draft content here..."
    )

    if st.button("Check Quality", key="quality_button"):
        if not quality_input.strip():
            st.warning("Paste content to review first.")
        else:
            prompt = f"""
Review this project reporting content:

{quality_input}

Evaluate it using this structure:

## Alignment Score
Score from 1 to 5.

## Activity-Focused Issues
Identify anything that sounds like task reporting instead of outcome reporting.

## Missing Metrics
Identify missing measurable data.

## Recommended Rewrite
Rewrite the content to be clearer, measurable, and leadership-ready.

## Final Readiness Decision
Ready / Needs Revision

Rules:
- Be direct.
- Do not rewrite with fake metrics.
- Clearly explain what would make the content stronger.
"""
            with st.spinner("Checking quality..."):
                result = ask_openai(prompt)
                st.markdown(result)