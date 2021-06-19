FROM python:3.6

ARG postgres_user
ARG postgres_password
ARG postgres_db

ENV POSTGRES_USER=$postgres_user
ENV POSTGRES_PASSWORD=$postgres_password
ENV POSTGRES_DB=$postgres_db
ENV POSTGRES_HOST=postgres
ENV POSTGRES_PORT=5432

RUN pip install psycopg2-binary
RUN pip install pygrametl

COPY ./src/ /app/
WORKDIR /app/

EXPOSE 5432