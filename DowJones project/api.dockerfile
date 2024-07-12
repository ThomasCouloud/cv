# api.dockerfile
FROM python:3.9-slim

WORKDIR /api

COPY requirements.txt /api/
RUN pip install --upgrade pip && pip install -r requirements.txt
RUN pip install python-multipart

COPY ./api /api

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]
