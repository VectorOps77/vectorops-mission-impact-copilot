from src.services.document_service import create_docx, build_docx_filename


def test_create_docx_returns_bytes():
    docx_data = create_docx(
        title="Test Report",
        content="## Executive Summary\nThis is a test document.",
        doc_type="MSR Draft",
        prepared_by="VectorOps",
    )

    assert isinstance(docx_data, bytes)
    assert docx_data[:2] == b"PK"


def test_build_docx_filename():
    filename = build_docx_filename("Test Report", "MSR Draft")

    assert filename.endswith(".docx")
    assert "test-report" in filename
