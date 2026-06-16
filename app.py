import streamlit as st

from src.llm.client import ask_openai
from src.services.prompts import (
    story_prompt,
    kpi_prompt,
    monthly_update_prompt,
    quality_check_prompt,
)

st.set_page_config(
    page_title="VectorOps Mission Impact Copilot",
    page_icon="📊",
    layout="wide",
)

st.title("📊 VectorOps Mission Impact Copilot")

st.write(
    "Turn raw project notes into outcome-based stories, KPIs, "
    "monthly updates, and leadership-ready MSR content."
)

st.warning(
    "AI-generated content must be reviewed by a human before being used in any official report."
)

tab1, tab2, tab3, tab4 = st.tabs(
    [
        "Story Assistant",
        "KPI Builder",
        "Monthly Update Assistant",
        "Quality Checker",
    ]
)

with tab1:
    st.header("Story Creation Assistant")

    story_input = st.text_area(
        "Enter raw project idea or problem statement",
        height=220,
        placeholder=(
            "Example: Reporting is manual and inconsistent. "
            "Leadership lacks clear visibility into risks, outcomes, and project health."
        ),
    )

    if st.button("Generate Story", key="story_button"):
        if not story_input.strip():
            st.warning("Enter a project idea first.")
        else:
            with st.spinner("Generating story..."):
                result = ask_openai(story_prompt(story_input))
                st.markdown(result)

with tab2:
    st.header("KPI Builder")

    kpi_input = st.text_area(
        "Enter KPI idea",
        height=220,
        placeholder=(
            "Example: Reduce the time required to create monthly project reports "
            "by using AI to draft outcome-based updates."
        ),
    )

    if st.button("Generate KPI", key="kpi_button"):
        if not kpi_input.strip():
            st.warning("Enter a KPI idea first.")
        else:
            with st.spinner("Building KPI..."):
                result = ask_openai(kpi_prompt(kpi_input))
                st.markdown(result)

with tab3:
    st.header("Monthly Update Assistant")

    update_input = st.text_area(
        "Paste raw monthly update notes",
        height=260,
        placeholder=(
            "Example: Built Power BI report, fixed data refresh issue, "
            "met with stakeholders, improved weekly reporting visibility."
        ),
    )

    if st.button("Generate Monthly Update", key="monthly_button"):
        if not update_input.strip():
            st.warning("Enter monthly update notes first.")
        else:
            with st.spinner("Generating monthly update..."):
                result = ask_openai(monthly_update_prompt(update_input))
                st.markdown(result)

with tab4:
    st.header("Quality & Alignment Checker")

    quality_input = st.text_area(
        "Paste story, KPI, or MSR content to review",
        height=260,
        placeholder="Paste generated or draft content here...",
    )

    if st.button("Check Quality", key="quality_button"):
        if not quality_input.strip():
            st.warning("Paste content to review first.")
        else:
            with st.spinner("Checking quality..."):
                result = ask_openai(quality_check_prompt(quality_input))
                st.markdown(result)