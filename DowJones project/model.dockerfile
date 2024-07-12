FROM python:3.9-slim

WORKDIR /model_training

ENV RUNNING_IN_DOCKER=True

COPY requirements.txt /model_training/
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY ./api /model_training/

CMD ["python", "model_training.py"]
