from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from http import HTTPStatus
from io import BytesIO
from app.pdf import extract_text_directly, extract_text_from_image
from app.preprocessing import preprocess
from app.stream import create_text_stream



app = FastAPI()

origins = ["http://localhost", "http://127.0.0.1"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health-check")
def ping():
    response = {
        "status-code": HTTPStatus.OK,
        "data": {},
    }
    return response

@app.post("/pdf-extract/")
async def extract_pdf(file: UploadFile):
    pdf = await file.read()
    pdf_bin = BytesIO(pdf)

    extracted_text, is_success = extract_text_directly(pdf_bin)
    if not is_success:
      extracted_text = extract_text_from_image(pdf)
    
    cleaned_text = preprocess(extracted_text)
   
    return StreamingResponse(create_text_stream(cleaned_text), media_type="text/plain")