from dbld_sql_queries import * 
from dbld_constantes import *  
from dbld_conexao import *  


con1 = conecta_db_sqlserver(servidor1,banco1,usuario1,senha1)
cursor1 = con1.cursor()


#sufixo = 0
#arquivo_tabelas = open('tabelas.txt') # onde está a lista de tabelas do SQL Server

nome_arq_tabs_sql = 'tabelas_sql.txt' 
str_query = 'query_select_t'
nome_query = ''
sqlq = ' '
tabelas = []
indice = 0
sufixo = ''


arquivo_tabelas = open(nome_arq_tabs_sql, encoding='utf-8-sig') # onde está a lista de tabelas do SQL Server

for line in arquivo_tabelas:
	if len(str(line)) > 6:
		#print('(1)-------------------------------')
		#print(line)
		tabelas.append(str(line).strip('\n'))


for tabela in tabelas:

	arquivo_tab = open(tabela,'w+')
	# iterar sufixo para que percorra todas as query_select_txx	
	#indice = indice + 1

	pos = tabela.find(".T")
	sufixo = str(tabela[pos+2:pos+4])
	nome_query = str_query + sufixo

	#sufixo = str(indice)
	#if len(str(indice)) == 1:
	#	sufixo = '0' + str(indice)
	
	#nome_query = str_query + sufixo 
	#print (eval(nome_query))
	
	cursor1.execute(eval(nome_query))
	
	rows = cursor1.fetchall()
	
	for row in rows:
		print('(2)-------------------------------')
		#print(row)
		linha_registro = []

		tamanho = len(row)
		for reg in range(tamanho):
			linha_registro.append(row[reg])
		
		if (sufixo) == '01':
			linha_registro[1] = processString(linha_registro[1])
			
		#arquivo_tab.write(str(row)+'\n')
		arquivo_tab.write(str(linha_registro)+'\n')

		print('(3)-------------------------------')		
		print(linha_registro)
		print (row)


#con2.commit()
con1.close()
