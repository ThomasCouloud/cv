# monitoring.dockerfile
FROM python:3.9

COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt

COPY ./monitoring .
COPY ./monitoring/encrypted_credentials.dat /encrypted_credentials.dat
COPY ./monitoring/secret.key /secret.key

CMD ["python", "/monitoring.py"]
