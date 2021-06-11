FROM postgres

ENV POSTGRES_USER=dwuser
ENV POSTGRES_PASSWORD=dwpass
ENV POSTGRES_DB=dw

COPY ./src/dw_tables.sql /docker-entrypoint-initdb.d/

EXPOSE 5432