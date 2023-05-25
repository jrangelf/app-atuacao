def processString(txt):
  specialChars = ",-.:?}{]/_[@!#$%^&*()" 
  for specialChar in specialChars:
    txt = txt.replace(specialChar, '')
  return txt


# Dados conexão sql server
SQL_USER = 'SVC_PGU_ATUACAO_WEB'
SQL_PASSWORD = 'QS07O$nCFFD5*uJegaZ'
SQL_SERVER = '10.207.112.5'
SQL_DB = 'PGU_ESTATISTICA'
SQL_PORT = 1433

# Dados conexão postgres
usuario2 = 'postgres'
senha2 = 'brasilia'
servidor2 = 'pgsql'
banco2 = 'atuacao'


retira = lambda a: a.split(';')

