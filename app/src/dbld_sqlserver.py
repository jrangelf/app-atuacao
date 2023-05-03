from src.dbld_sql_queries import * 
from src.dbld_constantes import *  
from src.dbld_conexao import *   


def selectRegistroSQL(valor,tipo):
	debug ("============ selectRegistroSQL =================")
	_regs = []

	con1 = conecta_db_sqlserver(servidor1,banco1,usuario1,senha1)
	cursor1 = con1.cursor()

	query = eval('query_select_registro_sql_' + tipo)
	query = query.replace('@',str(valor)) 

	debug('--------query-------')
	debug(query)
	
	cursor1.execute(query)	
	row_sql = cursor1.fetchone()

	debug('------row_sql--------')
	debug(row_sql)

	con1.close()
	return row_sql


def insertRegistroSQL(record_to_insert):

    con1 = conecta_db_sqlserver(servidor1,banco1,usuario1,senha1)
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

    return id_processo

