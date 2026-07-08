import streamlit as st

from src.llm.client import ask_openai
from src.services.prompts import (
    story_prompt,
    kpi_prompt,
    monthly_update_prompt,
    quality_check_prompt,
)
from src.services.document_service import create_docx, build_docx_filename
from src.config.prompt_library import PROMPT_LIBRARY
from src.config.schema_library import SCHEMA_LIBRARY

st.set_page_config(
    page_title="VectorOps Mission Impact Copilot",
    page_icon="📊",
    layout="wide",
)

st.title("📊 VectorOps Mission Impact Copilot")
st.write(
    "Turn raw project notes into outcome-based stories, KPIs, "
    "monthly updates, leadership-ready MSR content, and downloadable Word documents."
)

st.warning(
    "AI-generated content must be reviewed by a human before being used in any official report."
)

if "last_output" not in st.session_state:
    st.session_state.last_output = ""
if "last_output_title" not in st.session_state:
    st.session_state.last_output_title = "VectorOps PM Report"
if "last_output_type" not in st.session_state:
    st.session_state.last_output_type = "PM Report"


def save_last_output(title: str, doc_type: str, content: str) -> None:
    st.session_state.last_output_title = title
    st.session_state.last_output_type = doc_type
    st.session_state.last_output = content


tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(
    [
        "Story Assistant",
        "KPI Builder",
        "Monthly Update Assistant",
        "Quality Checker",
        "Document Generator",
        "AI Studio",
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
                save_last_output("Outcome-Based Project Story", "Project Story", result)
                st.markdown(result)
                st.success("Story saved to Document Generator tab.")

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
                save_last_output("KPI Summary", "KPI Report", result)
                st.markdown(result)
                st.success("KPI output saved to Document Generator tab.")

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
                save_last_output("Monthly Status Update", "MSR Draft", result)
                st.markdown(result)
                st.success("Monthly update saved to Document Generator tab.")

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
                save_last_output("Quality Alignment Review", "Quality Review", result)
                st.markdown(result)
                st.success("Quality review saved to Document Generator tab.")

with tab5:
    st.header("Document Generator")
    st.write("Create a polished Word document from the latest AI output or pasted content.")

    col1, col2 = st.columns(2)
    with col1:
        doc_title = st.text_input("Document Title", value=st.session_state.last_output_title)
        prepared_by = st.text_input("Prepared By", value="VectorOps")
    with col2:
        doc_type = st.selectbox(
            "Document Type",
            [
                "MSR Draft",
                "Project Story",
                "KPI Report",
                "Quality Review",
                "Executive Brief",
                "Status Report",
                "Meeting Summary",
            ],
            index=0 if st.session_state.last_output_type not in ["Project Story", "KPI Report", "Quality Review"] else [
                "MSR Draft", "Project Story", "KPI Report", "Quality Review", "Executive Brief", "Status Report", "Meeting Summary"
            ].index(st.session_state.last_output_type),
        )
        subtitle = st.text_input("Subtitle", value="AI-generated draft for human review")

    doc_content = st.text_area(
        "Document Content",
        value=st.session_state.last_output,
        height=380,
        placeholder="Generate content from one of the assistant tabs or paste content here...",
    )

    if not doc_content.strip():
        st.info("Generate content from another tab first, or paste document content above.")
    else:
        docx_bytes = create_docx(
            title=doc_title,
            content=doc_content,
            doc_type=doc_type,
            prepared_by=prepared_by,
            subtitle=subtitle,
        )
        filename = build_docx_filename(doc_title, doc_type)

        st.download_button(
            label="⬇️ Download Word Document",
            data=docx_bytes,
            file_name=filename,
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        )

        with st.expander("Preview content going into the document"):
            st.markdown(doc_content)

with tab6:
    st.header("AI Studio")
    st.write("Use pre-built prompts and schema guides to generate structured project, DevSecOps, and Azure documentation.")

    selected_prompt_name = st.selectbox(
        "Choose a Prompt",
        list(PROMPT_LIBRARY.keys()),
    )

    selected_prompt = PROMPT_LIBRARY[selected_prompt_name]
    selected_schema = SCHEMA_LIBRARY.get(selected_prompt_name, {})

    st.subheader(selected_prompt_name)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### When to Use")
        st.write(selected_prompt["when_to_use"])

        st.markdown("### Category")
        st.write(selected_prompt["category"])

        st.markdown("### Recommended Document Type")
        st.write(selected_prompt["document_type"])

    with col2:
        st.markdown("### Expected Schema")
        required_sections = selected_schema.get("required_sections", [])

        if required_sections:
            for section in required_sections:
                st.write(f"- {section}")
        else:
            st.info("No schema available for this prompt yet.")

    with st.expander("View Prompt Template"):
        st.code(selected_prompt["prompt"], language="markdown")

    studio_input = st.text_area(
        "Paste notes for this prompt",
        height=260,
        placeholder="Paste project notes, meeting notes, deployment notes, pipeline details, or rough ideas here...",
    )

    if st.button("Generate with AI Studio"):
        if not studio_input.strip():
            st.warning("Please paste notes first.")
        else:
            full_prompt = f"""
{selected_prompt["prompt"]}

User Notes:
{studio_input}
"""

            with st.spinner("Generating structured output..."):
                result = ask_openai(full_prompt)

            save_last_output(
                title=selected_prompt_name,
                doc_type=selected_prompt["document_type"],
                content=result,
            )

            st.success("Generated output saved to Document Generator.")
            st.markdown(result)