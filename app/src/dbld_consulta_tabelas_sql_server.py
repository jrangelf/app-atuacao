from datetime import datetime, date
from src.dbld_sql_queries import * 
from src.dbld_constantes import *  
from src.dbld_conexao import *  


class SQLData():
	
    def conexao():	    
        conn = conecta_db_sqlserver(SQL_SERVER,SQL_DB,SQL_USER,SQL_PASSWORD) 
        return conn
    
    @classmethod
    def selecionaTabela(self, sufixo: str):
        self.sufixo = sufixo
        str_query = 'query_select_t' + self.sufixo
        con = SQLData.conexao()
        cursor = con.cursor()
        cursor.execute(eval(str_query))
        rows = cursor.fetchall()
        con.close()
        return rows
    
    @classmethod    
    def selecionaColunas(self, tabela: str, colunai: int, colunad: int):
        
        self.tabela = tabela
        self.colunai = colunai
        self.colunad = colunad

        """ Este método busca os valores das colunas que contêm os códigos (colunai) 
        e as descrições (colunad) de cada tabela do banco SQLServer Atuação para serem 
        utilizados como opções nos campos de seleção. Recebe como parametro de entrada
        o número referente a tabela do SQL que se quer obter os valores, bem como as 
        colunas do código e da descricao, retona um dicionário: {'índice': 'descrição}"""
    
        _indice = 0
        _valores={}
        rows = SQLData.selecionaTabela(self.tabela)
    
        """ a tabela dos responsáveis possui dois campos como chave primária, por isso
        o índice do dicionário foi alterado por um contador, além disso, somente o
        código (1) deve ser selcionado."""
    
        for row in rows:
            if self.tabela=="14":
                if row[0]==1:
                    _indice += 1
                    _valores[_indice]=row[self.colunad]
            else:    		
                _valores[row[self.colunai]]=row[self.colunad]
    
        return _valores

    
    @classmethod
    def selecionaRegistro(self, valor,tipo):
        debug ("============ selecionaRegistro =================")
        
        self.valor = str(valor)
        self.tipo = tipo
        query = eval('query_select_registro_sql_' + self.tipo)
        str_query = query.replace('@', self.valor)
        
        debug('--------queries-------')
        debug(query)
        debug(str_query)

        con = SQLData.conexao()
        cursor = con.cursor()
        cursor.execute(str_query)
        row = cursor.fetchone()
        
        debug('------row_sql--------')
        debug(row)

        debug ("==================================================")

        con.close()
        return row

    """
    def insertRegistrosSQL(record_to_insert):

        con1 = conecta_db_sqlserver(SQL_SERVER,SQL_DB,SQL_USER,SQL_PASSWORD)
        cursor1 = con1.cursor()

        record_to_insert[13] = record_to_insert[13].replace('.','')
        record_to_insert[14] = record_to_insert[14].replace('.','')

        record_to_insert[13] = record_to_insert[13].replace(',','.')
        record_to_insert[14] = record_to_insert[14].replace(',','.')



        #debug ("------query_insert_registro_sqlserver-------")
        #debug (query_insert_registro_sqlserver)
        debug ("(1)------record_to_insert---------------(insertRegistroSQL)")
        debug(record_to_insert)
        
        _records = tuple(record_to_insert)
        debug("(1)-------_records")
        debug(_records)

        debug(query_insert_registro_sqlserver)

        cursor1.execute(query_insert_registro_sqlserver, _records)
        con1.commit()

        debug("(1)----registro inserido--------")


        debug("(2)---buscar o id do registro no banco sqlserver------")

        query = query_registro_inserido_sql_id.replace('@',str(record_to_insert[2]))
        query = query.replace('$',str(record_to_insert[12]))
        query = query.replace('%',str(record_to_insert[18]))
        query = query.replace('^',str(record_to_insert[10]))  

        debug (query)

        cursor1.execute(query)	
        row_sqlid = cursor1.fetchone()
    
        debug("(3)-----fetch--------")
        debug(row_sqlid)

        id_processo = row_sqlid[0]

        debug("(4)----id_processo------------")
        debug (id_processo)
        con1.close()
        return id_processo"""
    
    @classmethod
    def formatarListaRegistros(self, registros: list,
                               instancia: dict,
                               origemprocesso: dict,
                               tipocalculo: dict,
                               objetoacao: dict,
                               unidade: dict,
                               valores: dict):
        
        """ este método formata os campos para persistir na tabela principal
            do banco atuação no SQLServerver. A lista registros possui 17 
            campos do POST, mas a tabela T01_PROCESSO possui 21 parâmetros.
            Retorna uma lista com os valores formatados para serem gravados
            na tabela T01_PROCESSO. 
            
            registros = [
                        'csrfmiddlewaretoken', 
                        'Situação da União', 
                        'N. do processo', 
                        'Nome do autor', 
                        'Instância', 
                        'Origem do processo', 
                        'Quant. exequentes', 
                        'Tipo de cálculo', 
                        'Objeto da ação', 
                        'Unidade', 
                        'N. do parecer', 
                        'Valor da União', 
                        'Valor do Autor', 
                        'Data de envio para unidade', 
                        'Data de saída', 
                        'Nome responsavel', 
                        'Observação']

            
            
            
            
            """
        
        self.regs = registros
        self.instancia = instancia
        self.origemprocesso = origemprocesso
        self.tipocalculo = tipocalculo
        self.objetoacao = objetoacao
        self.unidade = unidade
        self.valores = valores

                
        # retirar o 'csrfmiddlewaretoken'
        self.regs.remove(self.regs[0])		
        self.regs[0]= '2' if self.regs[0] == 'Autora' else '1'		
		
		# fixar em N - Cálculo
        self.regs.insert(1,'N')		
		
        cod_instancia = getKeyByValue(self.instancia, self.valores['instancia'])
        self.regs[4]=int(cod_instancia)
		
        cod_origem_processo = getKeyByValue(self.origemprocesso, self.valores['origemprocesso'])
        self.regs[5]=int(cod_origem_processo)		
		
        cod_tipo_calculo = getKeyByValue(self.tipocalculo, self.valores['tipocalculo'])
        self.regs[7]=int(cod_tipo_calculo)
		
        cod_objeto_acao = getKeyByValue(self.objetoacao, self.valores['objeto'])
        self.regs[8]=int(cod_objeto_acao)		
		
		# fixar em 1 - Advocacia-Geral da União
        self.regs.insert(9,1)		
		
        cod_unidade = getKeyByValue(self.unidade, self.valores['unidade'])
        self.regs[10] = int(cod_unidade)
		
		# com a desterritorialização somente há um tipo de parecer (conclusivo)
        self.regs.insert(11,1)

		# inserir nulo para o prazo do advogado
        self.regs.insert(16,None)

        data_atual = date.today()
        self.regs.append(str(data_atual))

        return self.regs


        
 


def buscaValoresSQLServer(tabela: str, colunai: int, colunad: int):
    
    """ Este método busca os valores dos códigos e das descrições 
    no banco do Atuação (SQLServer) para serem utilizados
    como opções nos campos de seleção.
    Recebe como parametro de entrada o número referente a tabela 
    do SQL que se quer obter os valores, bem como as colunas do 
    índice e da descricao, retona um dicionário: {'índice': 'descrição}"""
    
    _indice = 0
    _valores={}
    rows = SQLData.selecionaTabela(tabela)
    
    """ a tabela dos responsáveis possui dois campos como chave primária, por isso
    o índice do dicionário foi alterado por um contador, além disso, somente o
    código (1) deve ser selcionado."""
    
    for row in rows:
        if tabela=="14":
            if row[0]==1:
                _indice=_indice+1
                _valores[_indice]=row[colunad]
        else:    		
            _valores[row[colunai]]=row[colunad]
    
    return _valores
    
def obtemIndiceSQLServer(dicionario: dict, valor: str):
    """ retona a chave"""
    pass


def getKeyByValue(dicionario: dict, valor: str):
    _lista = [k for k,v in dicionario.items() if v == valor]
    return str(_lista[0])






"""
            
cursor1.execute(eval(nome_query))
	
	rows = cursor1.fetchall()
	
	for row in rows:
		print('(2)-------------------------------')
		#print(row)
	    
	    
nome_query = ''
sqlq = ' '
tabelas = []
indice = 0
sufixo = ''



con = conecta_db_sqlserver(SQL_SERVER,SQL_DB,SQL_USER,SQL_PASSWORD)
cursor = con.cursor()


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
"""