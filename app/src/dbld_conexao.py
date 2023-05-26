import psycopg2
import pymssql
from src.conf_debug import *


def conecta_db_sqlserver(server,db,username,password):
    debug("conecta_db_sqlserver")
    try:
        conn = pymssql.connect(host=server, database=db, user=username, password=password)
    except pymssql.Error as erro:
        error("Falha de conexão com SQL Server " + db, erro) 
    finally:
        return conn





