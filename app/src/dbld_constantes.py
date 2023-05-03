def processString(txt):
  specialChars = ",-.:?}{]/_[@!#$%^&*()" 
  for specialChar in specialChars:
    txt = txt.replace(specialChar, '')
  return txt


# Dados conexão sql server
usuario1 = 'SVC_PGU_ATUACAO_WEB'
senha1 = 'QS07O$nCFFD5*uJegaZ'
servidor1 = '10.207.112.5'
banco1 = 'PGU_ESTATISTICA'
porta = 1433

# Dados conexão postgres
usuario2 = 'postgres'
senha2 = 'brasilia'
servidor2 = 'localhost'
banco2 = 'atuacao'


retira = lambda a: a.split(';')

