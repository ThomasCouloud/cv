# data.dockerfile
FROM python:3.9-slim

WORKDIR /LoadData

COPY requirements.txt /LoadData/
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY ./LoadData /LoadData

CMD ["python", "LoadRecurentData.py"]
