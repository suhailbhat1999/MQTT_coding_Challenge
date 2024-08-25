FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install gmqtt

EXPOSE 1883

CMD ["python", "./mqtt_reader.py"]
