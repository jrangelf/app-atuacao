from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from src.dbld_sql_server import *


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

		debug("------valores--------")
		debug(valores)
		debug("---------------------")
		
		for valor in valores.values():
			lista_registros.append(valor)
			
		debug("----lista_registros antes----")
		debug(lista_registros)
		
		lista_regs_formatada = SQLData.formatarListaRegistros(
								lista_registros,
								instancia,
								origemprocesso,
								tipocalculo,
								objetoacao,
								unidade,
								valores)

		sql_id = SQLData.gravarRegistro(lista_regs_formatada)
		registro = SQLData.selecionaRegistro(sql_id, "id")
		
		_situacaouniao = "Ré" if registro[7] == 1 else "Autora"		
		_instancia = instancia[Decimal(registro[4])]
		_origemprocesso = origemprocesso[Decimal(registro[6])]
		_tipocalculo = tipocalculo[Decimal(registro[8])]
		_objetoacao = objetoacao[Decimal(registro[9])]		
		_unidade = unidade[Decimal(registro[23])]		

		msg = 'Registro inserido com sucesso!'  
		messages.success (request, (msg))

		
		return render(request,'entradadados.html',{'inseridos':'inseridos',
													'registro':registro,
													'instancia':_instancia,													
													'origem':_origemprocesso,
													'situacaouniao':_situacaouniao,
													'tipocalculo':_tipocalculo,
													'objetoacao':_objetoacao,
													'necap':_unidade
													})

	else:
	
		contexto['instancia']=instancia
		contexto['origemprocesso'] = origemprocesso
		contexto['tipocalculo']=tipocalculo
		contexto['objetoacao']=objetoacao		
		contexto['unidade']=unidade
		contexto['responsavel']=responsavel
				
		return render(request, 'entradadados.html', context=contexto)


def home(request):	
	return render(request,'home.html',{})


def consulta(request):

	if request.method == "POST":
		# fazer um trim no _proc
		_proc = str(request.POST.get('numproc'))
		_id = request.POST.get('idproc')
		
		if (_proc =="") and (_id ==""):
			return render(request,'consulta.html',{})
		valor = _proc if _proc != "" else _id
		tipo = "numproc" if _proc != "" else "id"
		#registro = selectRegistroSQL(valor, tipo)		 

	return render(request,'consulta.html',{})


def relatorios(request):
	return render(request,'relatorios.html',{})
