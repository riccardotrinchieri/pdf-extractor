FROM ubuntu:22.04

WORKDIR /pdf-extractor


RUN apt-get update -y && \
    apt-get install -y python3.9 && \
    apt-get install -y poppler-utils && \
    apt-get install -y  tesseract-ocr && \
    apt-get clean

RUN apt update -y && \
    apt install -y python3-pip

COPY ./requirements.txt /pdf-extractor/requirements.txt

RUN pip3 install -r requirements.txt

COPY ./app /pdf-extractor/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]