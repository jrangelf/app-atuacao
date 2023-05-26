from decouple import config, Csv

def processString(txt):
  specialChars = ",-.:?}{]/_[@!#$%^&*()" 
  for specialChar in specialChars:
    txt = txt.replace(specialChar, '')
  return txt


# Dados conexão sql server
#SQL_USER = 'SVC_PGU_ATUACAO_WEB'
#SQL_PASSWORD = 'QS07O$nCFFD5*uJegaZ'
#SQL_SERVER = '10.207.112.5'
#SQL_DB = 'PGU_ESTATISTICA'
#SQL_PORT = 1433

# Dados conexão sql server
SQL_USER = config('SQL_USER')
SQL_PASSWORD = config('SQL_PASSWORD')
SQL_SERVER = config('SQL_SERVER')
SQL_DB = config('SQL_DB')
SQL_PORT = config('SQL_PORT')


retira = lambda a: a.split(';')

