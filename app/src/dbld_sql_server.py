from decimal import Decimal
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
        """ ID(0)
            NUM_PROCESSO(1)            
            NOME EXEQUENTE(2
            QUANTIDADE EXEQUENTES(3)
            COD INSTANCIA(4)
            COD ORGAO REPRESENTADO(5)
            COD UNIDADE(6)
            COD SITUACAO UNIAO(7)
            COD TIPO CALCULO(8)
            COD OBJETO ACAO(9)
            COD TIPO PARECER(10)
            NUM PARECER(11)
            VR AUTOR(12)
            VR UNIAO(13)
            DT ENVIO NECAP(14)
            DT PRAZO ADVOGADO(15)
            DT RECEBIMENTO TECNICO(16)
            DT SAIDA NECAP(17)
            OBSERVACAO(18)
            NOME RESPONSAVEL(19)
            SN PERICIA(20)
            DT DIGITACAO(21)
            NUM ACAO ORIGINARIA(22)
            COD DESC NECAP(23)"""
        
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

    
    @classmethod
    def gravarRegistro(self, record_to_insert: list):

        """recebe a lista com os campos formatados e grava o registro no banco 
           SQLServer retornando o id do registro gravado"""

        self.record = record_to_insert

        """retirar ponto separador de milhar e substituir vírgula por ponto
        nos valores da União e do Autor"""

        self.record[13] = self.record[13].replace('.','')
        self.record[14] = self.record[14].replace('.','')

        self.record[13] = self.record[13].replace(',','.')
        self.record[14] = self.record[14].replace(',','.')

        debug ("(1)------record_to_insert---------------")
        debug(self.record)
        
        _records = tuple(self.record)

        debug("(2)-------tuple(record_to_insert)--------")
        debug(_records)
        debug("(3)----query_insert_registro_sqlserver-----")
        debug(query_insert_registro_sqlserver)

        con = SQLData.conexao()
        cursor = con.cursor()

        cursor.execute(query_insert_registro_sqlserver, _records)
        con.commit()
               
        debug("(4)-------registro inserido--------")
        debug("(1)---buscar o id do registro no banco sqlserver------")

        str_query = query_registro_inserido_sql_id.replace('@',str(self.record[2]))
        str_query = str_query.replace('$',str(self.record[12]))
        str_query = str_query.replace('%',str(self.record[18]))
        str_query = str_query.replace('^',str(self.record[10]))  

        debug("(2)-----query de busca--------------")
        debug (str_query)

        cursor.execute(str_query)	
        row_sqlid = cursor.fetchone()
    
        debug("(3)-----registro inserido--------")
        debug(row_sqlid)

        id_processo = row_sqlid[0]

        debug("(4)----id_processo------------")
        debug (id_processo)
        con.close()

        return id_processo
    

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
 

def getKeyByValue(dicionario: dict, valor: str):
    _lista = [k for k,v in dicionario.items() if v == valor]
    return str(_lista[0])

