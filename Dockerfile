FROM python:3.11-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY PD1.py .

ENV FLASK_APP=PD1

EXPOSE 5000
CMD ["python", "PD1.py"]
