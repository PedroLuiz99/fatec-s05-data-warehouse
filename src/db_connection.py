from os import getenv
import psycopg2
import pygrametl

dw_string = f"host='{getenv('POSTGRES_HOST')}' " \
            f"dbname='{getenv('POSTGRES_DB')}' " \
            f"user='{getenv('POSTGRES_USER')}' " \
            f"password='{getenv('POSTGRES_PASSWORD')}' "
dw_pgconn = psycopg2.connect(dw_string)
dw_conn_wrapper = pygrametl.ConnectionWrapper(connection=dw_pgconn)
