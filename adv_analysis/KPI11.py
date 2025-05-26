import os
from fastapi.responses import FileResponse

KPI11_FILE_PATH = "KPI_Data\KPI 11.docx"

def get_docx_file_response():
    if not os.path.exists(KPI11_FILE_PATH):
        return None
    return FileResponse(
        path=KPI11_FILE_PATH,
        media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        filename="KPI-11.docx"
    )