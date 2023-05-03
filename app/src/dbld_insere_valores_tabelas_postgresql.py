
import datetime
import decimal
from decimal import Decimal 

from dbld_sql_queries import * 
from dbld_constantes import *  
from dbld_conexao import *  


nome_arq_tabs_sql = 'tabelas_sql.txt'
str_query = 'query_insert_t'
nome_query = ''
sqlq = ' '
pos=0
nome_arquivos_tabelas = []
nome_arquivos_dados = []
tabelas_postgres = []
indice = 0
sufixo = ''

try:
	arquivo_tabelas = open(nome_arq_tabs_sql)

except (Exception, psycopg2.Error) as error:
    print("Falha ao tentar abrir o arquivo " + nome_arq_tabs_sql, error)

finally:
	if arquivo_tabelas:
		print("Dados do arquivo de tabelas foram obtidos")



try:
   
    con2 = conecta_db_postgre(servidor2,banco2,usuario2,senha2)
    cursor2 = con2.cursor()

    for line in arquivo_tabelas:

	    if len(str(line)) > 6:

			#obtém o nome de cada arquivo onde estão os dados.

		    str_line = str(line).strip('\n')
		    print ('(1)---str_line ---------------------------')
		    print (str_line)
		    print ('------------------------------------------')

			# abre o arquivo de dados 
		    arquivo_dados = open(str_line)

			# busca a query correspondente
		    pos = str_line.find(".T")
		    sufixo = str(str_line[pos+2:pos+4])
		    nome_query = str_query + sufixo
		    print ('(2)------------------------------')
		    print (nome_query)
		    print ('------------------------------------------')

		    for dado in arquivo_dados:
		    #for y in range(3,6,1):

		        print ('(3)------------------------------')
		        print (dado)
		        print(type(dado))
		        print ('------------------------------------------')

		    
		        novalista = []
		        for elemento in eval(dado):
		        	novalista.append(elemento)

		        print('(4)----novalista--------------------')
		        print(type(novalista))
		        print(novalista)
		        print ('------------------------------------------')


		        postgres_insert_query = eval(nome_query)
		        print ('(5)--postgres_insert_query-------------------------')
		        print (postgres_insert_query)
		        print ('------------------------------------------')

		        record_to_insert = novalista
		        print ('(6)--record_to_insert----------------------------')
		        print (record_to_insert)
		        print ('------------------------------------------')	        
		        

		        cursor2.execute(postgres_insert_query, record_to_insert)

			
		    con2.commit()
		    conta = cursor2.rowcount
		    print(conta, "Registro inserido com sucesso")


except (Exception, psycopg2.Error) as error:
    print("Falha ao inserir o registro na tabela: ", error)

finally:
    # closing database connection.
    if con2:
        cursor2.close()
        con2.close()
        print("Conexão com PostgreSQL encerrada")