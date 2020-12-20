FROM registry.access.redhat.com/ubi8/python-38 
LABEL maintainer="Lonnie Gerol <lonnie@lonniegerol.com>"

WORKDIR /opt/dining

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "dining:app", "--workers 4", "--bind=0.0.0.0:8080", "--access-logfile=-"]
