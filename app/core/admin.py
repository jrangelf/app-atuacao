from django.contrib import admin
from .models import  Teste, Tribunais, T01Processo,	T02TipoCalculo, T03Instancia, T04OrigemProcesso,\
					T05SituacaoUniaoProcesso, T06TipoParecer, T07ObjetoAcao, T08OrgaoRepresentado,\
					T09Necap, T14ResponsavelProcesso
 
class TesteAdmin(admin.ModelAdmin):
	list_display = ('nome','sobrenome','estado')
	orderby = ('nome',)


class TribunaisAdmin(admin.ModelAdmin):
	list_display = ['nome', 'sigla']
	orderby = ['nome']


class T01ProcessoAdmin(admin.ModelAdmin):
    list_display = [

    't01_id_processo',
	't01_num_processo',
	't01_nome_exequente', 
	't01_qtd_exequente',
	't01_cod_instancia',
	't01_cod_orgao_representado',
	't01_cod_unidade',
	't01_cod_situacao_uniao',
	't01_cod_tipo_calculo',
	't01_cod_objeto_acao', 
	't01_cod_tipo_parecer',
	't01_num_parecer', 
	't01_vr_autor', 
	't01_vr_uniao', 
	't01_dt_envio_necap',
	't01_dt_prazo_advogado',
	't01_dt_recebimento_tecnico',
	't01_dt_saida_necap', 
	't01_obs_processo', 
	't01_nome_responsavel',
	't01_sn_pericia', 
	't01_dt_digitacao', 
	't01_num_acao_originaria',
	't01_desc_necap']



admin.site.register(Teste)
admin.site.register(Tribunais)

admin.site.register(T01Processo)
admin.site.register(T02TipoCalculo)
admin.site.register(T03Instancia)
admin.site.register(T04OrigemProcesso)
admin.site.register(T05SituacaoUniaoProcesso)
admin.site.register(T06TipoParecer)
admin.site.register(T07ObjetoAcao)
admin.site.register(T08OrgaoRepresentado)
admin.site.register(T09Necap)
admin.site.register(T14ResponsavelProcesso)
