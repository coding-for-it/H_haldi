from fastapi import APIRouter
from fastapi.responses import PlainTextResponse
from docx import Document

router = APIRouter()

def read_kpi4_docx(docx_path: str = "KPI_Data\KPI 4 representation.docx") -> str:
    """
    Reads the KPI-4-representation.docx file and returns its text content.
    """
    try:
        doc = Document(docx_path)
        full_text = []
        for para in doc.paragraphs:
            full_text.append(para.text)
        return '\n'.join(full_text)
    except Exception as e:
        return f"Error reading document: {str(e)}"

@router.get("/kpi4/docs", response_class=PlainTextResponse)
def kpi4_docs():
    doc_text = read_kpi4_docx()
    if not doc_text.strip() or doc_text.startswith("Error reading document:"):
        return PlainTextResponse("No content available in the document.", status_code=404)
    return PlainTextResponse(doc_text)