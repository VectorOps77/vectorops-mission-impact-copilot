import streamlit as st

from src.config.document_templates import DOCUMENT_TEMPLATES
from src.config.prompt_library import PROMPT_LIBRARY
from src.config.schema_library import SCHEMA_LIBRARY
from src.llm.client import ask_openai
from src.services.document_service import build_docx_filename, create_docx
from src.services.prompts import (
    kpi_prompt,
    monthly_update_prompt,
    quality_check_prompt,
    story_prompt,
)


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
    "AI-generated content must be reviewed by a human before being used "
    "in any official report."
)


# -------------------------------------------------------------------
# Session state
# -------------------------------------------------------------------

if "last_output" not in st.session_state:
    st.session_state.last_output = ""

if "last_output_title" not in st.session_state:
    st.session_state.last_output_title = "VectorOps PM Report"

if "last_output_type" not in st.session_state:
    st.session_state.last_output_type = "MSR Report"


def save_last_output(title: str, doc_type: str, content: str) -> None:
    """
    Save the most recent AI-generated output so it can be reused
    in the Document Generator tab.
    """
    st.session_state.last_output_title = title
    st.session_state.last_output_type = doc_type
    st.session_state.last_output = content


def get_template_index(template_names: list[str], saved_type: str) -> int:
    """
    Return the correct dropdown index for the saved document type.

    Older parts of the app may save names such as 'Project Story'
    or 'MSR Draft', while the new template library uses names such
    as 'Executive Brief' and 'MSR Report'.
    """
    template_mapping = {
        "MSR Draft": "MSR Report",
        "Project Story": "Executive Brief",
        "KPI Report": "KPI Report",
        "Quality Review": "Technical Report",
        "Executive Brief": "Executive Brief",
        "Status Report": "MSR Report",
        "Meeting Summary": "Meeting Summary",
        "DevSecOps Report": "DevSecOps Report",
        "Technical Report": "Technical Report",
    }

    mapped_type = template_mapping.get(saved_type, saved_type)

    if mapped_type in template_names:
        return template_names.index(mapped_type)

    return 0


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


# -------------------------------------------------------------------
# Tab 1: Story Assistant
# -------------------------------------------------------------------

with tab1:
    st.header("Story Creation Assistant")

    story_input = st.text_area(
        "Enter raw project idea or problem statement",
        height=220,
        placeholder=(
            "Example: Reporting is manual and inconsistent. "
            "Leadership lacks clear visibility into risks, outcomes, "
            "and project health."
        ),
        key="story_input",
    )

    if st.button("Generate Story", key="story_button"):
        if not story_input.strip():
            st.warning("Enter a project idea first.")
        else:
            with st.spinner("Generating story..."):
                result = ask_openai(story_prompt(story_input))

            save_last_output(
                title="Outcome-Based Project Story",
                doc_type="Executive Brief",
                content=result,
            )

            st.markdown(result)
            st.success("Story saved to the Document Generator tab.")


# -------------------------------------------------------------------
# Tab 2: KPI Builder
# -------------------------------------------------------------------

with tab2:
    st.header("KPI Builder")

    kpi_input = st.text_area(
        "Enter KPI idea",
        height=220,
        placeholder=(
            "Example: Reduce the time required to create monthly project "
            "reports by using AI to draft outcome-based updates."
        ),
        key="kpi_input",
    )

    if st.button("Generate KPI", key="kpi_button"):
        if not kpi_input.strip():
            st.warning("Enter a KPI idea first.")
        else:
            with st.spinner("Building KPI..."):
                result = ask_openai(kpi_prompt(kpi_input))

            save_last_output(
                title="KPI Summary",
                doc_type="KPI Report",
                content=result,
            )

            st.markdown(result)
            st.success("KPI output saved to the Document Generator tab.")


# -------------------------------------------------------------------
# Tab 3: Monthly Update Assistant
# -------------------------------------------------------------------

with tab3:
    st.header("Monthly Update Assistant")

    update_input = st.text_area(
        "Paste raw monthly update notes",
        height=260,
        placeholder=(
            "Example: Built Power BI report, fixed data refresh issue, "
            "met with stakeholders, and improved weekly reporting visibility."
        ),
        key="monthly_update_input",
    )

    if st.button("Generate Monthly Update", key="monthly_button"):
        if not update_input.strip():
            st.warning("Enter monthly update notes first.")
        else:
            with st.spinner("Generating monthly update..."):
                result = ask_openai(monthly_update_prompt(update_input))

            save_last_output(
                title="Monthly Status Update",
                doc_type="MSR Report",
                content=result,
            )

            st.markdown(result)
            st.success("Monthly update saved to the Document Generator tab.")


# -------------------------------------------------------------------
# Tab 4: Quality Checker
# -------------------------------------------------------------------

with tab4:
    st.header("Quality & Alignment Checker")

    quality_input = st.text_area(
        "Paste story, KPI, or MSR content to review",
        height=260,
        placeholder="Paste generated or draft content here...",
        key="quality_input",
    )

    if st.button("Check Quality", key="quality_button"):
        if not quality_input.strip():
            st.warning("Paste content to review first.")
        else:
            with st.spinner("Checking quality..."):
                result = ask_openai(quality_check_prompt(quality_input))

            save_last_output(
                title="Quality Alignment Review",
                doc_type="Technical Report",
                content=result,
            )

            st.markdown(result)
            st.success("Quality review saved to the Document Generator tab.")


# -------------------------------------------------------------------
# Tab 5: Document Generator
# -------------------------------------------------------------------

with tab5:
    st.header("Document Generator")

    st.write(
        "Create a polished Word document from the latest AI output "
        "or from content you paste manually."
    )

    template_names = list(DOCUMENT_TEMPLATES.keys())

    col1, col2 = st.columns(2)

    with col1:
        doc_title = st.text_input(
            "Document Title",
            value=st.session_state.last_output_title,
            key="document_title",
        )

        prepared_by = st.text_input(
            "Prepared By",
            value="VectorOps",
            key="prepared_by",
        )

    with col2:
        selected_template_name = st.selectbox(
            "Document Template",
            template_names,
            index=get_template_index(
                template_names,
                st.session_state.last_output_type,
            ),
            key="document_template",
        )

        subtitle = st.text_input(
            "Subtitle",
            value="AI-generated draft for human review",
            key="document_subtitle",
        )

    selected_template = DOCUMENT_TEMPLATES[selected_template_name]

    st.caption(selected_template["description"])

    with st.expander("View selected template sections"):
        for section in selected_template["sections"]:
            st.write(f"- {section}")

    doc_content = st.text_area(
        "Document Content",
        value=st.session_state.last_output,
        height=380,
        placeholder=(
            "Generate content from one of the assistant tabs "
            "or paste document content here..."
        ),
        key="document_content",
    )

    if not doc_content.strip():
        st.info(
            "Generate content from another tab first, "
            "or paste document content above."
        )
    else:
        docx_bytes = create_docx(
            title=doc_title,
            content=doc_content,
            doc_type=selected_template_name,
            prepared_by=prepared_by,
            subtitle=subtitle,
        )

        filename = build_docx_filename(
            doc_title,
            selected_template_name,
        )

        st.download_button(
            label="⬇️ Download Word Document",
            data=docx_bytes,
            file_name=filename,
            mime=(
                "application/vnd.openxmlformats-officedocument."
                "wordprocessingml.document"
            ),
            key="download_word_document",
        )

        with st.expander("Preview content going into the document"):
            st.markdown(doc_content)


# -------------------------------------------------------------------
# Tab 6: AI Studio
# -------------------------------------------------------------------

with tab6:
    st.header("AI Studio")

    st.write(
        "Choose a reusable AI prompt and a document template, "
        "then generate structured project, cloud, DevSecOps, "
        "or leadership documentation."
    )

    prompt_col, template_col = st.columns(2)

    with prompt_col:
        selected_prompt_name = st.selectbox(
            "Choose an AI Prompt",
            list(PROMPT_LIBRARY.keys()),
            key="studio_prompt",
        )

    with template_col:
        studio_template_name = st.selectbox(
            "Choose an Output Document Template",
            list(DOCUMENT_TEMPLATES.keys()),
            key="studio_template",
        )

    selected_prompt = PROMPT_LIBRARY[selected_prompt_name]
    selected_schema = SCHEMA_LIBRARY.get(selected_prompt_name, {})
    studio_template = DOCUMENT_TEMPLATES[studio_template_name]

    st.subheader(selected_prompt_name)

    info_col1, info_col2, info_col3 = st.columns(3)

    with info_col1:
        st.markdown("### When to Use")
        st.write(selected_prompt["when_to_use"])

    with info_col2:
        st.markdown("### Category")
        st.write(selected_prompt["category"])

        st.markdown("### Recommended Type")
        st.write(selected_prompt["document_type"])

    with info_col3:
        st.markdown("### Selected Template")
        st.write(studio_template_name)
        st.caption(studio_template["description"])

    schema_col, template_sections_col = st.columns(2)

    with schema_col:
        st.markdown("### Prompt Schema")

        required_sections = selected_schema.get(
            "required_sections",
            [],
        )

        if required_sections:
            for section in required_sections:
                st.write(f"- {section}")
        else:
            st.info("No schema is currently available for this prompt.")

    with template_sections_col:
        st.markdown("### Output Template Sections")

        for section in studio_template["sections"]:
            st.write(f"- {section}")

    with st.expander("View AI prompt instructions"):
        st.code(
            selected_prompt["prompt"],
            language="markdown",
        )

    studio_input = st.text_area(
        "Paste notes for this prompt",
        height=260,
        placeholder=(
            "Paste project notes, meeting notes, deployment details, "
            "pipeline information, risks, accomplishments, or rough ideas..."
        ),
        key="studio_input",
    )

    if st.button(
        "Generate with AI Studio",
        key="studio_generate_button",
    ):
        if not studio_input.strip():
            st.warning("Please paste notes first.")
        else:
            template_sections = "\n".join(
                f"## {section}"
                for section in studio_template["sections"]
            )

            full_prompt = f"""
{selected_prompt["prompt"]}

You must format the final response using the selected document template.

Selected document template:
{studio_template_name}

Required output sections:
{template_sections}

Instructions:
- Use every required section.
- Keep the section headings exactly as provided.
- Do not add unrelated sections.
- Use clear, professional language.
- Focus on measurable mission or business impact.
- Do not invent facts, dates, metrics, or accomplishments.
- When information is missing, state that it was not provided.

User Notes:
{studio_input}
"""

            with st.spinner(
                f"Generating {studio_template_name}..."
            ):
                result = ask_openai(full_prompt)

            save_last_output(
                title=selected_prompt_name,
                doc_type=studio_template_name,
                content=result,
            )

            st.success(
                "Generated output saved to the Document Generator tab."
            )

            st.markdown(result)