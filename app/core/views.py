from django.shortcuts import render
#from datetime import datetime, date
from django.contrib import messages

from django.http import HttpResponse

from src.dbld_sql_queries import * 
from src.dbld_constantes import *  
from src.dbld_conexao import *  
from src.dbld_sqlserver import *
from src.dbld_consulta_tabelas_sql_server import *

#from src.configura_debug import *

def entradadados(request):
	
	contexto = {}
	instancia={}
	origemprocesso={}
	tipocalculo={}
	objetoacao={}
	unidade={}

	"""seleciona o código e a descrição das tabelas do SQLServer"""
	instancia = SQLData.selecionaColunas('03',0,1)
	origemprocesso = SQLData.selecionaColunas('04',0,4)
	tipocalculo = SQLData.selecionaColunas('02',0,1)
	objetoacao = SQLData.selecionaColunas('07',0,1)
	unidade = SQLData.selecionaColunas('09',0,1)
	responsavel = SQLData.selecionaColunas('14',0,1)

	if request.method == "POST":
		
		lista_registros = []	
		valores = dict(request.POST.items())

		print("------valores--------")
		print(valores)
		print("---------------------")
		
		for valor in valores.values():
			lista_registros.append(valor)
			
		print("----lista_registros antes----")
		print(lista_registros)
		
		lista_regs_formatada = SQLData.formatarListaRegistros(
								lista_registros,
								instancia,
								origemprocesso,
								tipocalculo,
								objetoacao,
								unidade,
								valores)

		sql_id = insertRegistroSQL(lista_regs_formatada)

		registro = SQLData.selecionaRegistro(sql_id, "id")

		print(registro)

		 

		"""

		
		sql_id = insertRegistroSQL(lista_registros)

		# buscar o registro que foi gravado para visualização
		registro = selectRegistroSQL(sql_id, "id")

		instancia = T03Instancia.objects.get(t03_id_instancia =registro[4])
		orgaorepresentado = T08OrgaoRepresentado.objects.get(t08_id_orgao_representado =registro[5])
		origem = T04OrigemProcesso.objects.get(t04_id_unidade=registro[6])
		situacaouniao = "Ré" if registro[7]==1 else "Autora"
		tipocalculo = T02TipoCalculo.objects.get(t02_id_tipo_calculo =registro[8])
		objetoacao = T07ObjetoAcao.objects.get(t07_id_objeto_acao =registro[9])
		tipoparecer = T06TipoParecer.objects.get(t06_id_tipo_parecer =registro[10])
		necap = T09Necap.objects.get(t09_id_necap =registro[23])	

		return render(request, 'teste.html', {'valores':valores})

		
		#msg = 'Registro inserido com sucesso!'  
		#messages.success (request, (msg))
		#return render(request, 'teste.html', context=contexto)
		)"""

		return render(request, 'entradadados.html', {'valores':valores})

	else:
	
		contexto['instancia']=instancia
		contexto['origemprocesso'] = origemprocesso
		contexto['tipocalculo']=tipocalculo
		contexto['objetoacao']=objetoacao
		#contexto['orgaorepresentado']=orgaorepresentado
		contexto['unidade']=unidade
		contexto['responsavel']=responsavel
				
		return render(request, 'entradadados.html', context=contexto)


def teste(request):	
	return render(request, 'teste.html',{})

def teste2(request):
	if request.method == "POST":
		
		valores = dict(request.POST.items())

		print("valores recebidos")
		print(valores)		

	return render(request, 'teste2.html',{'valores':valores})


def home(request):
	first_name = "DCP"
	last_name = "Brasília-DF"
	return render(request,'home.html',{})

"""
def entradadadosX(request):

	lista_instancia =[]
	lista_origemprocesso = []
	lista_orgaorepresentado =[]
	lista_unidade = []
	lista_tipocalculo =[]
	lista_objetoacao = []
	lista_tipoparecer = []

	if request.method == "POST":
		
		lista_registros = []
		
		valores = dict(request.POST.items())
		print(valores)
		for valor in valores.values():
			lista_registros.append(valor)
			print(valor)
		
		lista_registros.remove(lista_registros[0])
		
		print("===== lista_registros =======")
		print(lista_registros)	
		
		lista_registros[0]= "2" if lista_registros[0] == "Autora" else "1"
		 
		lista_registros[1] = "S" if lista_registros[1] == "Perícia" else "N"
		
		cod_tipo_parecer =T06TipoParecer.objects.all().filter(t06_desc_tipo_parecer =lista_registros[11])	
		lista_registros[11]=cod_tipo_parecer.values()[0]['t06_id_tipo_parecer']

			
		cod_instancia = T03Instancia.objects.all().filter(t03_sigla_instancia=lista_registros[4])
		lista_registros[4]=cod_instancia.values()[0]['t03_id_instancia']

		cod_origem_processo = T04OrigemProcesso.objects.all().filter(t04_sigla_unidade=lista_registros[5])
		lista_registros[5]=cod_origem_processo.values()[0]['t04_id_unidade']

		cod_tipo_calculo = T02TipoCalculo.objects.all().filter(t02_desc_tipo_calculo=lista_registros[7])
		lista_registros[7]=cod_tipo_calculo.values()[0]['t02_id_tipo_calculo']

		cod_objeto_acao = T07ObjetoAcao.objects.all().filter(t07_desc_objeto_acao=lista_registros[8])
		lista_registros[8]=cod_objeto_acao.values()[0]['t07_id_objeto_acao']

		cod_orgao_representado = T08OrgaoRepresentado.objects.all().filter(t08_desc_orgao_representado=lista_registros[9])
		lista_registros[9]=cod_orgao_representado.values()[0]['t08_id_orgao_representado']
		
		cod_unidade = T09Necap.objects.all().filter(t09_desc_necap=lista_registros[10])
		lista_registros[10] = cod_unidade.values()[0]['t09_id_necap'] 
					
		data_atual = date.today()
		print("data de digitação: " + str(data_atual))
		print("---------------------")

		# inserir a data de digitação
		lista_registros.append(str(data_atual))
		print("---lista_registros---")
		print(lista_registros)
		print("---------------------")



		sql_id = insertRegistroSQL(lista_registros)

		# buscar o registro que foi gravado para visualização
		registro = selectRegistroSQL(sql_id, "id")

		instancia = T03Instancia.objects.get(t03_id_instancia =registro[4])
		orgaorepresentado = T08OrgaoRepresentado.objects.get(t08_id_orgao_representado =registro[5])
		origem = T04OrigemProcesso.objects.get(t04_id_unidade=registro[6])
		situacaouniao = "Ré" if registro[7]==1 else "Autora"
		tipocalculo = T02TipoCalculo.objects.get(t02_id_tipo_calculo =registro[8])
		objetoacao = T07ObjetoAcao.objects.get(t07_id_objeto_acao =registro[9])
		tipoparecer = T06TipoParecer.objects.get(t06_id_tipo_parecer =registro[10])
		necap = T09Necap.objects.get(t09_id_necap =registro[23])	



		msg = 'Registro inserido com sucesso!'  
		messages.success (request, (msg))


		
		return render(request,'entradadados.html',{'inseridos':'inseridos',
													'registro':registro,
													'instancia':instancia,
													'orgaorepresentado':orgaorepresentado,
													'origem':origem,
													'situacaouniao':situacaouniao,
													'tipocalculo':tipocalculo,
													'objetoacao':objetoacao,
													'tipoparecer':tipoparecer,
													'necap':necap
													})

	else:

		#aqui tem-se que usar a funcao retira para retirar o código numérico

		processos = T01Processo.objects.all()

		tipocalculo = T02TipoCalculo.objects.all()
		for i in range(tipocalculo.count()):
			lista_tipocalculo.append(tipocalculo.values()[i]['t02_desc_tipo_calculo'])
		
		instancia = T03Instancia.objects.all()
		for i in range(instancia.count()):
			lista_instancia.append(instancia.values()[i]['t03_sigla_instancia'])

		origemprocesso = T04OrigemProcesso.objects.all()
		for i in range(origemprocesso.count()):
			lista_origemprocesso.append(origemprocesso.values()[i]['t04_sigla_unidade'])

		tipoparecer = T06TipoParecer.objects.all()
		for i in range(tipoparecer.count()):
			lista_tipoparecer.append(tipoparecer.values()[i]['t06_desc_tipo_parecer'])

		objetoacao = T07ObjetoAcao.objects.all()
		for i in range(objetoacao.count()):
			lista_objetoacao.append(objetoacao.values()[i]['t07_desc_objeto_acao'])
		
		orgaorepresentado = T08OrgaoRepresentado.objects.all()
		for i in range(orgaorepresentado.count()):
			lista_orgaorepresentado.append(orgaorepresentado.values()[i]['t08_desc_orgao_representado'])
		
		necap = T09Necap.objects.all()
		for i in range(necap.count()):
			lista_unidade.append(necap.values()[i]['t09_desc_necap'])
		
		responsavelprocesso = T14ResponsavelProcesso.objects.all()
		

		return render(request,'entradadados.html', {'processos':processos,
													'tipocalculo':lista_tipocalculo,
													'instancia':lista_instancia,
													'origemprocesso':lista_origemprocesso,
													'tipoparecer':lista_tipoparecer,
													'objetoacao':lista_objetoacao,
													'orgaorepresentado':lista_orgaorepresentado,
													'necap':lista_unidade,
													'responsavelprocesso':responsavelprocesso
													})
"""

def consulta(request):

	if request.method == "POST":

		# fazer um trim no _proc

		_proc = str(request.POST.get('numproc'))
		_id = request.POST.get('idproc')
		
		if (_proc =="") and (_id ==""):
			return render(request,'consulta.html',{})


		valor = _proc if _proc != "" else _id
		tipo = "numproc" if _proc != "" else "id"


		registro = selectRegistroSQL(valor, tipo)		 

		

	return render(request,'consulta.html',{})



def relatorios(request):
	return render(request,'relatorios.html',{})
