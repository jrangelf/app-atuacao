import psycopg2
import pymssql
from src.conf_debug import *

"""
def conecta_db_sqlserver(server,db,username,pwd):
	
	try:
		conn = pyodbc.connect(driver='{SQL Server}', 
							host=server, 
							database=db,
							user=username, 
							password=pwd)

	except (Exception, pyodbc.Error) as error:
		print("Falha de conexão com SQL Server " + db, error)

	finally:
		return conn
"""


def conecta_db_sqlserver(server,db,username,password):

    debug("conecta_db_sqlserver")
    try:
        conn = pymssql.connect(host=server, database=db, user=username, password=password)

    except pymssql.Error as error:
        print("Falha de conexão com SQL Server " + db, error)
    
    finally:
        return conn



def conecta_db_postgre(server,db,username,pwd):
	debug ("conecta_db_postgre")
	conn = psycopg2.connect(host=server,
							database=db,
							user=username,
							password=pwd)
	return conn



