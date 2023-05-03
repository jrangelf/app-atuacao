import datetime
import decimal

from decimal import Decimal 

from dbld_sql_queries import * 
from dbld_constantes import *  
from dbld_conexao import *   




nome_arq_tabs_sql = 'tabelas_insercao.txt' 
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
    arquivo_tabelas = open(nome_arq_tabs_sql, encoding='utf-8-sig') #encoding='utf-8'

except (Exception, psycopg2.Error) as error:
    print("Falha ao tentar abrir o arquivo " + nome_arq_tabs_sql, error)

finally:
    if arquivo_tabelas:
        print("Dados do arquivo de tabelas foram obtidos")


try:
    con2 = conecta_db_postgre(servidor2,banco2,usuario2,senha2)
    cursor2 = con2.cursor()
    registro = 0

    for line in arquivo_tabelas:

        if len(str(line)) > 6:

			#obtém o nome de cada arquivo onde estão os dados.

            str_line = str(line).strip('\n')

			# abre o arquivo de dados 
            arquivo_dados = open(str_line)

            print ('----------------------------str_line---(1)')
            print (str_line)
            print ('------------------------------------------')

			# busca a query correspondente
            pos = str_line.find(".T")
            sufixo = str(str_line[pos+2:pos+4])
            nome_query = str_query + sufixo
            postgres_insert_query = eval(nome_query)

            for dado in arquivo_dados:

                novalista = []
                for elemento in eval(dado):
                   novalista.append(elemento)

                record_to_insert = novalista

                cursor2.execute(postgres_insert_query, record_to_insert)
                
                registro = registro + 1

            con2.commit()
            print(registro,"Registros inseridos com sucesso")
		

except (Exception, psycopg2.Error) as error:
    print("Falha ao inserir o registro na tabela: ", error)

finally:
    # closing database connection.
    if con2:
        cursor2.close()
        con2.close()
        print("Conexão com PostgreSQL encerrada")