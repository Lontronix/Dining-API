FROM python:3.8-alpine
LABEL maintainer="Lonnie Gerol <lonnie@lonniegerol.com>"

WORKDIR /opt/dining

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "dining:app". "--bind=0.0.0.0:8080", "--access-logfile=-"]
