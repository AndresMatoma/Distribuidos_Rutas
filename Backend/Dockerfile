FROM python:3.10.6

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt
RUN pip install psycopg2-binary
RUN apt-get update && apt-get install -y postgresql-client


COPY . .
