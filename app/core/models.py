from django.db import models
from django import forms

"""
class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
"""

NOME_GRATIFICACAO = (
	('GDATA','GDATA'),
	('GDPGTAS','GDPGTAS'),
	('GDASST','GDASST'),
	('GDPGPE','GDPGPE'),
	)



class Teste(models.Model):

    nome = models.CharField('Nome', max_length=20)
    sobrenome = models.CharField('Sobrenome', max_length=30)
    estado =  models.CharField('Estado', max_length=5)

    class Meta:
        verbose_name = '1. Nome'
        verbose_name_plural = '1. Nomes'

    def __str__(self):
        return self.nome + '  ' + self.sobrenome + '  ' + self.estado


class Tribunais(models.Model):

    nome = models.CharField('Tribunal', max_length=30)
    sigla = models.CharField('Sigla', max_length=10)

    class Meta:
        verbose_name = '2. Tribunal'
        verbose_name_plural = '2. Tribunais'

    def __str__(self):
        return self.nome + '  ' + self.sigla


class T01Processo(models.Model):
    t01_id_processo = models.AutoField(db_column='T01_ID_PROCESSO', primary_key=True)  # Field name made lowercase.
    t01_num_processo = models.CharField(db_column='T01_NUM_PROCESSO', max_length=30)  # Field name made lowercase.
    t01_nome_exequente = models.CharField(db_column='T01_NOME_EXEQUENTE', max_length=70, blank=True, null=True)  # Field name made lowercase.
    t01_qtd_exequente = models.IntegerField(db_column='T01_QTD_EXEQUENTE', blank=True, null=True)  # Field name made lowercase.
    t01_cod_instancia = models.ForeignKey('T03Instancia', models.DO_NOTHING, db_column='T01_COD_INSTANCIA', blank=True, null=True)  # Field name made lowercase.
    t01_cod_orgao_representado = models.ForeignKey('T08OrgaoRepresentado', models.DO_NOTHING, db_column='T01_COD_ORGAO_REPRESENTADO', blank=True, null=True)  # Field name made lowercase.
    t01_cod_unidade = models.ForeignKey('T04OrigemProcesso', models.DO_NOTHING, db_column='T01_COD_UNIDADE', blank=True, null=True)  # Field name made lowercase.
    t01_cod_situacao_uniao = models.ForeignKey('T05SituacaoUniaoProcesso', models.DO_NOTHING, db_column='T01_COD_SITUACAO_UNIAO', blank=True, null=True)  # Field name made lowercase.
    t01_cod_tipo_calculo = models.ForeignKey('T02TipoCalculo', models.DO_NOTHING, db_column='T01_COD_TIPO_CALCULO', blank=True, null=True)  # Field name made lowercase.
    t01_cod_objeto_acao = models.ForeignKey('T07ObjetoAcao', models.DO_NOTHING, db_column='T01_COD_OBJETO_ACAO', blank=True, null=True)  # Field name made lowercase.
    t01_cod_tipo_parecer = models.ForeignKey('T06TipoParecer', models.DO_NOTHING, db_column='T01_COD_TIPO_PARECER', blank=True, null=True)  # Field name made lowercase.
    t01_num_parecer = models.CharField(db_column='T01_NUM_PARECER', max_length=20, blank=True, null=True)  # Field name made lowercase.
    t01_vr_autor = models.FloatField(db_column='T01_VR_AUTOR', blank=True, null=True)  # Field name made lowercase.
    t01_vr_uniao = models.FloatField(db_column='T01_VR_UNIAO', blank=True, null=True)  # Field name made lowercase.
    t01_dt_envio_necap = models.DateTimeField(db_column='T01_DT_ENVIO_NECAP', blank=True, null=True)  # Field name made lowercase.
    t01_dt_prazo_advogado = models.DateTimeField(db_column='T01_DT_PRAZO_ADVOGADO', blank=True, null=True)  # Field name made lowercase.
    t01_dt_recebimento_tecnico = models.DateTimeField(db_column='T01_DT_RECEBIMENTO_TECNICO', blank=True, null=True)  # Field name made lowercase.
    t01_dt_saida_necap = models.DateTimeField(db_column='T01_DT_SAIDA_NECAP', blank=True, null=True)  # Field name made lowercase.
    t01_obs_processo = models.CharField(db_column='T01_OBS_PROCESSO', max_length=200, blank=True, null=True)  # Field name made lowercase.
    t01_nome_responsavel = models.CharField(db_column='T01_NOME_RESPONSAVEL', max_length=70, blank=True, null=True)  # Field name made lowercase.
    t01_sn_pericia = models.CharField(db_column='T01_SN_PERICIA', max_length=1, blank=True, null=True)  # Field name made lowercase.
    t01_dt_digitacao = models.DateTimeField(db_column='T01_DT_DIGITACAO', blank=True, null=True)  # Field name made lowercase.
    t01_num_acao_originaria = models.CharField(db_column='T01_NUM_ACAO_ORIGINARIA', max_length=30, blank=True, null=True)  # Field name made lowercase.
    t01_desc_necap = models.DecimalField(db_column='T01_DESC_NECAP', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        verbose_name = 'T01 - Dados do Processo'
        verbose_name_plural = 'T01 - Dados dos Processos'
        ordering = ['-t01_id_processo']

    def __str__(self):
        return str(self.t01_num_processo) + ' -- ' + str(self.t01_nome_exequente)

class T02TipoCalculo(models.Model):
    t02_id_tipo_calculo = models.AutoField(db_column='T02_ID_TIPO_CALCULO', primary_key=True)  # Field name made lowercase.
    t02_desc_tipo_calculo = models.CharField(db_column='T02_DESC_TIPO_CALCULO', max_length=70, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        verbose_name = 'T02 - Tipo de Cálculo'
        verbose_name_plural = 'T02 - Tipos de Cálculo'
        ordering = ['t02_desc_tipo_calculo']

    def __str__(self):
        return self.t02_desc_tipo_calculo #+ ';' + str(self.t02_id_tipo_calculo)


class T03Instancia(models.Model):
    t03_id_instancia = models.AutoField(db_column='T03_ID_INSTANCIA', primary_key=True)  # Field name made lowercase.
    t03_sigla_instancia = models.CharField(db_column='T03_SIGLA_INSTANCIA', max_length=4, blank=True, null=True)  # Field name made lowercase.
    t03_tipo_atuacao_tribunal = models.CharField(db_column='T03_TIPO_ATUACAO_TRIBUNAL', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        verbose_name = 'T03 - Tipo de Instância'
        verbose_name_plural = 'T03 - Tipos de Instâncias'
        ordering = ['t03_sigla_instancia']

    def __str__(self):
        return str(self.t03_sigla_instancia) #+ ';' + str(self.t03_id_instancia)


class T04OrigemProcesso(models.Model):
    t04_id_unidade = models.AutoField(db_column='T04_ID_UNIDADE', primary_key=True)  # Field name made lowercase.
    t04_num_ordem = models.DecimalField(db_column='T04_NUM_ORDEM', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    t04_num_regiao = models.CharField(db_column='T04_NUM_REGIAO', max_length=3, blank=True, null=True)  # Field name made lowercase.
    t04_desc_unidade = models.CharField(db_column='T04_DESC_UNIDADE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    t04_sigla_unidade = models.CharField(db_column='T04_SIGLA_UNIDADE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    t04_nome_cidade_unidade = models.CharField(db_column='T04_NOME_CIDADE_UNIDADE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    t04_sigla_uf_unidade = models.CharField(db_column='T04_SIGLA_UF_UNIDADE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    t04_cod_necap = models.ForeignKey('T09Necap', models.DO_NOTHING, db_column='T04_COD_NECAP', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        verbose_name = 'T04 - Origem do Processo'
        verbose_name_plural = 'T04 - Origens do Processo'
        ordering = ['t04_sigla_unidade']

    def __str__(self):
        return str(self.t04_sigla_unidade) #+ ';' + str(self.t04_id_unidade)


class T05SituacaoUniaoProcesso(models.Model):
    t05_id_situacao_uniao = models.AutoField(db_column='T05_ID_SITUACAO_UNIAO', primary_key=True)  # Field name made lowercase.
    t05_desc_situacao_uniao = models.CharField(db_column='T05_DESC_SITUACAO_UNIAO', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        verbose_name = 'T05 - Situação da União'
        verbose_name_plural = 'T05 - Situação da União'

    def __str__(self):
        return self.t05_desc_situacao_uniao

class T06TipoParecer(models.Model):
    t06_id_tipo_parecer = models.AutoField(db_column='T06_ID_TIPO_PARECER', primary_key=True)  # Field name made lowercase.
    t06_desc_tipo_parecer = models.CharField(db_column='T06_DESC_TIPO_PARECER', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        verbose_name = 'T06 - Tipo de parecer'
        verbose_name_plural = 'T06 - Tipos de parecer'
        ordering = ['t06_desc_tipo_parecer']

    def __str__(self):
        return self.t06_desc_tipo_parecer #+ ';' + str(self.t06_id_tipo_parecer)

class T07ObjetoAcao(models.Model):
    t07_id_objeto_acao = models.AutoField(db_column='T07_ID_OBJETO_ACAO', primary_key=True)  # Field name made lowercase.
    t07_desc_objeto_acao = models.CharField(db_column='T07_DESC_OBJETO_ACAO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    t07_num_grupo = models.DecimalField(db_column='T07_NUM_GRUPO', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        verbose_name = 'T07 - Objeto da ação'
        verbose_name_plural = 'T07 - Objetos da ação'
        ordering = ['t07_desc_objeto_acao']

    def __str__(self):
        return self.t07_desc_objeto_acao  #+ ';' + str(self.t07_id_objeto_acao)


class T08OrgaoRepresentado(models.Model):
    t08_id_orgao_representado = models.AutoField(db_column='T08_ID_ORGAO_REPRESENTADO', primary_key=True)  # Field name made lowercase.
    t08_desc_orgao_representado = models.CharField(db_column='T08_DESC_ORGAO_REPRESENTADO', max_length=70, blank=True, null=True)  # Field name made lowercase.
    t08_cod_orgao_vinculado = models.DecimalField(db_column='T08_COD_ORGAO_VINCULADO', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    t08_sigla_abrangencia_demanda = models.CharField(db_column='T08_SIGLA_ABRANGENCIA_DEMANDA', max_length=6, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        verbose_name = 'T08 - Órgão representado'
        verbose_name_plural = 'T08 - Órgãos representado'
        ordering = ['t08_desc_orgao_representado']

    def __str__(self):
        return self.t08_desc_orgao_representado #+ ';' + str(self.t08_id_orgao_representado)


class T09Necap(models.Model):
    t09_id_necap = models.AutoField(db_column='T09_ID_NECAP', primary_key=True)  # Field name made lowercase.
    t09_desc_necap = models.CharField(db_column='T09_DESC_NECAP', max_length=50, blank=True, null=True)  # Field name made lowercase.
    t09_cod_senha = models.CharField(db_column='T09_COD_SENHA', max_length=8)  # Field name made lowercase.
    t09_cod_necap_regional = models.DecimalField(db_column='T09_COD_NECAP_REGIONAL', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    t09_cod_abrangencia_atuacao = models.CharField(db_column='T09_COD_ABRANGENCIA_ATUACAO', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        verbose_name = 'T09 - Lista NECAP'
        verbose_name_plural = 'T09 - Lista NECAPs'
        ordering = ['t09_desc_necap']

    def __str__(self):
        return self.t09_desc_necap #+ ';' + str(self.t09_id_necap)



class T14ResponsavelProcesso(models.Model):
    t14_id = models.AutoField(db_column='T14_ID', primary_key=True)  # Field name made lowercase.
    t14_cod_necap = models.ForeignKey('T09Necap', models.DO_NOTHING, db_column='T14_COD_NECAP', blank=True, null=True)
    t14_nome_responsavel = models.CharField(db_column='T14_NOME_RESPONSAVEL', max_length=70, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        verbose_name = 'T14 - Responsável Processo'
        verbose_name_plural = 'T14 - Responsável Processo'
        ordering = ['t14_nome_responsavel']
        #unique_together = (('t14_cod_necap', 't14_nome_responsavel'),)

    def __str__(self):
        #return self.t14_nome_responsavel + '   -   ' + str(self.t14_cod_necap)
        return self.t14_nome_responsavel 


