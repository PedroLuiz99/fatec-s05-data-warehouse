FROM postgres

ARG postgres_user
ARG postgres_password
ARG postgres_db

ENV POSTGRES_USER=$postgres_user
ENV POSTGRES_PASSWORD=$postgres_password
ENV POSTGRES_DB=$postgres_db

COPY ./src/dw_tables.sql /docker-entrypoint-initdb.d/

EXPOSE 5432