
from dbld_sql_queries import *
from dbld_constantes import *
from dbld_conexao import *

sql_id = 0
registro = 0

con1 = conecta_db_sqlserver(servidor1,banco1,usuario1,senha1)
cursor1 = con1.cursor()

con2 = conecta_db_postgre(servidor2,banco2,usuario2,senha2)
cursor2 = con2.cursor()

cursor1.execute(query_sql_count)
regs_sql = cursor1.fetchone()

cursor2.execute(query_postgres_count)
regs_postgres = cursor2.fetchone()

regsql, regpost = int(regs_sql[0]),int(regs_postgres[0]) 
diferenca = regsql-regpost

print ('Registros na tabela T01_PROCESSOS no SQL Server: ',regsql)
print ('Registros na tabela T01_PROCESSOS no PostgreSQL: ', regpost)
print ('Diferença: ', regsql-regpost)


if (diferenca) > 0:
	print ("Postgres deve ser atualizado")
	cursor1.execute(query_select_sqlserver.replace('@',str(diferenca)))
	rows_sql = cursor1.fetchall()

	for nome in rows_sql:
		print (nome[0], ' - ', nome[1], ' - ', nome[2])


elif (diferenca) < 0:
    print ("SQL deve ser atualizado")
    cursor2.execute(query_select_postgres)
    rows_postgres = cursor2.fetchall()
	
    for nome in rows_postgres:
        print (nome[0], ' - ', nome[1], ' - ', nome[2])
	
else:
	print ("Tabelas sincronizadas")

con1.close()
con2.close()
