from django import forms
#from tempus_dominus.widgets import DatePicker
from datetime import datetime
from .models import Teste, Tribunais, T01Processo

 
class TesteForm(forms.ModelForm):
	
	class Meta:
		model = Teste
		fields= ['nome', 'sobrenome', 'estado']


class TribunaisForm(forms.ModelForm):

	class Meta:
		model = Tribunais
		fields = ["Nome do Tribunal", "sigla"]


class ProcessoForm(forms.ModelForm):

	class Meta:
		model = Processo
		fields = ['t01_id_processo',
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
