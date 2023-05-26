# selection scripts

query_select_t01 = """
SELECT T01_ID_PROCESSO,T01_NUM_PROCESSO,T01_NOME_EXEQUENTE,T01_QTD_EXEQUENTE\
,T01_COD_INSTANCIA,T01_COD_ORGAO_REPRESENTADO,T01_COD_UNIDADE,T01_COD_SITUACAO_UNIAO\
,T01_COD_TIPO_CALCULO,T01_COD_OBJETO_ACAO,T01_COD_TIPO_PARECER,T01_NUM_PARECER\
,T01_VR_AUTOR,T01_VR_UNIAO,T01_DT_ENVIO_NECAP,T01_DT_PRAZO_ADVOGADO\
,T01_DT_RECEBIMENTO_TECNICO,T01_DT_SAIDA_NECAP,T01_OBS_PROCESSO,T01_NOME_RESPONSAVEL\
,T01_SN_PERICIA,T01_DT_DIGITACAO,T01_NUM_ACAO_ORIGINARIA,T01_DESC_NECAP \
FROM dbo.T01_PROCESSO
"""


query_select_t02 = """
SELECT T02_ID_TIPO_CALCULO, T02_DESC_TIPO_CALCULO \
FROM dbo.T02_TIPO_CALCULO \
ORDER BY T02_DESC_TIPO_CALCULO
"""


query_select_t03 = """
SELECT T03_ID_INSTANCIA, T03_SIGLA_INSTANCIA, T03_TIPO_ATUACAO_TRIBUNAL \
FROM dbo.T03_INSTANCIA \
ORDER BY T03_SIGLA_INSTANCIA
"""

query_select_t04 = """
SELECT T04_ID_UNIDADE,T04_NUM_ORDEM,T04_NUM_REGIÃO,T04_DESC_UNIDADE\
,T04_SIGLA_UNIDADE,T04_NOME_CIDADE_UNIDADE,T04_SIGLA_UF_UNIDADE,T04_COD_NECAP \
FROM dbo.T04_ORIGEM_PROCESSO \
ORDER BY T04_DESC_UNIDADE
"""


query_select_t05 = """
SELECT T05_ID_SITUACAO_UNIAO,T05_DESC_SITUACAO_UNIAO \
FROM dbo.T05_SITUACAO_UNIAO_PROCESSO
"""


query_select_t06 = """
SELECT T06_ID_TIPO_PARECER, T06_DESC_TIPO_PARECER \
FROM dbo.T06_TIPO_PARECER
"""


query_select_t07 = """ 
SELECT T07_ID_OBJETO_ACAO,T07_DESC_OBJETO_ACAO,T07_NUM_GRUPO \
FROM dbo.T07_OBJETO_ACAO \
ORDER BY T07_DESC_OBJETO_ACAO
"""


query_select_t08 = """
SELECT T08_ID_ORGAO_REPRESENTADO,T08_DESC_ORGAO_REPRESENTADO,T08_COD_ORGAO_VINCULADO\
,T08_SIGLA_ABRANGENCIA_DEMANDA \
FROM dbo.T08_ORGAO_REPRESENTADO
"""


query_select_t09 = """ 
SELECT T09_ID_NECAP,T09_DESC_NECAP,T09_COD_SENHA,T09_COD_NECAP_REGIONAL\
,T09_COD_ABRANGENCIA_ATUACAO \
FROM dbo.T09_NECAP
"""


query_select_t10 = """
SELECT T10_ANO_RECEITA_EFETIVA,T10_MES_RECEITA_EFETIVA,T10_COD_TIPO_RECOLHIMENTO,T10_VR_HONORARIO\
,T10_VR_INDENIZACAO \
FROM dbo.T10_RECEITA_EFETIVA
"""


query_select_t11 = """ 
SELECT T11_NUM_ANO,T11_QTD_PROCESSO_ANALISADO,T11_QTD_EXEQUENTE \
FROM dbo.T11_QUANTIDADE_HISTORICA
"""


query_select_t12 = """
SELECT T12_ID_SUGESTAO,T12_COD_NECAP,T12_NOME_SERVIDOR,T12_DT_SUGESTAO\
,T12_DESC_SUGESTAO,T12_DESC_RESPOSTA \
FROM dbo.T12_SUGESTAO_RESPOSTA
"""


query_select_t13 = """  
SELECT T13_COD_NECAP, T13_NUM_PROCESSO,T13_MES_ANO, T13_NUM_VARA\
,T13_NOME_AUTOR, T13_VR_PRINCIPAL, T13_VR_JUROS_MORA, T13_VR_PGTO_ADM\
,T13_PERC_DESCONTO, T13_DT_ENTRADA_DADOS \
FROM dbo.T13_FINANCEIRO_ACORDO
"""


query_select_t14 = """
SELECT T14_COD_NECAP,T14_NOME_RESPONSAVEL \
FROM dbo.T14_RESPONSAVEL_PROCESSO \
WHERE T14_COD_NECAP=1 \
ORDER BY T14_NOME_RESPONSAVEL
"""


query_select_t15 = """
SELECT T15_ID_PERITO, T15_NOME_PERITO, T15_COD_FORMACAO_PERITO, T15_COD_TIPO_ATUACAO_PERITO\
,T15_NUM_TELEFONE_PERITO, T15_DESC_ORGAO_REGISTRO_PERITO,T15_NUM_REGISTRO_ORGAO\
,T15_ENDERECO_RESIDENCIA_PERITO, T15_CIDADE_RESIDENCIA_PERITO, T15_UF_RESIDENCIA_PERITO \
FROM dbo.T15_PERITO
"""


query_select_t16 = """ 
SELECT T16_ID_FORMACAO_PERITO,T16_DESC_FORMACAO_PERITO \
FROM dbo.T16_FORMACAO_PERITO
"""


query_select_t17 = """
SELECT T17_ID_POSICAO_AGU_PROCESSO,T17_DESC_POSICAO_AGU_PROCESSO \
FROM dbo.T17_POSICAO_AGU_PROCESSO
"""


query_select_t18 = """
SELECT T18_ID_PROPOSTA_HONORARIO_PERICIA,T18_COD_PERITO,T18_COD_PROCESSO,T18_DT_PROPOSTA_PERITO\
,T18_DESC_ASSUNTO,T18_VR_PEDIDO_PERITO,T18_VR_AGU,T18_DT_PARECER\
,T18_COD_POSICAO_AGU_PROCESSO,T18_OBSERVACAO \
FROM dbo.T18_PROPOSTA_PERITO
"""


query_select_t19 = """
SELECT T19_ID_TIPO_RECOLHIMENTO_RECEITA,T19_DESC_TIPO_RECOLHIMENTO_RECEITA \
FROM dbo.T19_TIPO_RECOLHIMENTO_RECEITA
"""


query_select_t20 = """
SELECT T20_ID_TIPO_ATUACAO_PERITO,T20_DESC_TIPO_ATUACAO_PERITO \
FROM dbo.T20_TIPO_ATUACAO_PERITO
"""


query_select_t21 = """
SELECT T21_NUM_IDENTICACAO, T21_COD_SITUACAO_UNIAO, T21_SN_PERICIA, T21_COD_TIPO_CALCULO\
,T21_COD_OBJETO_ACAO, T21_DT_CADASTRAMENTO \
FROM dbo.T21_COMBINACAO_POSSIVEL_PROCESSO
"""

query_sql_count = 'SELECT count(T01_ID_PROCESSO) FROM dbo.T01_PROCESSO'

query_select_sqlserver = "SELECT TOP @ * FROM dbo.T01_PROCESSO ORDER BY T01_ID_PROCESSO DESC"

query_select_registro_sql_numproc = "SELECT * FROM dbo.T01_PROCESSO WHERE [T01_NUM_PROCESSO] = '@' "

#query_select_registro_sql_id = "SELECT * FROM dbo.T01_PROCESSO WHERE [T01_ID_PROCESSO] = @"
query_select_registro_sql_id = "SELECT * FROM dbo.T25_PROCESSO_TESTE WHERE [T01_ID_PROCESSO] = @"

#query_registro_inserido_sql_id = """SELECT [T01_ID_PROCESSO] FROM dbo.T01_PROCESSO WHERE [T01_NUM_PROCESSO] = '@' \
# AND [T01_NUM_PARECER] ='$'  AND [T01_NOME_RESPONSAVEL] = '%' AND [T01_DESC_NECAP] = '^' """

query_registro_inserido_sql_id = """SELECT [T01_ID_PROCESSO] FROM dbo.T25_PROCESSO_TESTE WHERE [T01_NUM_PROCESSO] = '@' \
 AND [T01_NUM_PARECER] ='$'  AND [T01_NOME_RESPONSAVEL] = '%' AND [T01_DESC_NECAP] = '^' """



# inserting scripts
# substituiu-se os '?' por '%s'
query_insert_registro_sqlserver = """

INSERT INTO dbo.T25_PROCESSO_TESTE
         ( T01_COD_SITUACAO_UNIAO
          ,T01_SN_PERICIA
          ,T01_NUM_PROCESSO
          ,T01_NOME_EXEQUENTE
          ,T01_COD_INSTANCIA
          ,T01_COD_UNIDADE
          ,T01_QTD_EXEQUENTE           
          ,T01_COD_TIPO_CALCULO
          ,T01_COD_OBJETO_ACAO
          ,T01_COD_ORGAO_REPRESENTADO
          ,T01_DESC_NECAP                                        
          ,T01_COD_TIPO_PARECER
          ,T01_NUM_PARECER
          ,T01_VR_AUTOR
          ,T01_VR_UNIAO
          ,T01_DT_ENVIO_NECAP
          ,T01_DT_PRAZO_ADVOGADO
          ,T01_DT_SAIDA_NECAP
          ,T01_NOME_RESPONSAVEL         
          ,T01_OBS_PROCESSO
          ,T01_DT_DIGITACAO) 
VALUES 
(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
"""


query_insert_t01 = """
INSERT INTO core_t01processo
           (\"T01_ID_PROCESSO\"
           ,\"T01_NUM_PROCESSO\"
           ,\"T01_NOME_EXEQUENTE\"
           ,\"T01_QTD_EXEQUENTE\"
           ,\"T01_COD_INSTANCIA\"
           ,\"T01_COD_ORGAO_REPRESENTADO\"
           ,\"T01_COD_UNIDADE\"
           ,\"T01_COD_SITUACAO_UNIAO\"
           ,\"T01_COD_TIPO_CALCULO\"
           ,\"T01_COD_OBJETO_ACAO\"
           ,\"T01_COD_TIPO_PARECER\"
           ,\"T01_NUM_PARECER\"
           ,\"T01_VR_AUTOR\"
           ,\"T01_VR_UNIAO\"
           ,\"T01_DT_ENVIO_NECAP\"
           ,\"T01_DT_PRAZO_ADVOGADO\"
           ,\"T01_DT_RECEBIMENTO_TECNICO\"
           ,\"T01_DT_SAIDA_NECAP\"
           ,\"T01_OBS_PROCESSO\"
           ,\"T01_NOME_RESPONSAVEL\"
           ,\"T01_SN_PERICIA\"
           ,\"T01_DT_DIGITACAO\"
           ,\"T01_NUM_ACAO_ORIGINARIA\"
           ,\"T01_DESC_NECAP\")
     VALUES
           (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
"""


query_insert_t02 = """  
INSERT INTO core_t02tipocalculo
           (\"T02_ID_TIPO_CALCULO\"
           ,\"T02_DESC_TIPO_CALCULO\")
     VALUES
           (%s,%s)
"""


query_insert_t03 = """
INSERT INTO core_t03instancia
           (\"T03_ID_INSTANCIA\"
           ,\"T03_SIGLA_INSTANCIA\"
           ,\"T03_TIPO_ATUACAO_TRIBUNAL\")
     VALUES
           (%s,%s,%s)
"""


query_insert_t04 = """
INSERT INTO core_t04origemprocesso
           (\"T04_ID_UNIDADE\"
           ,\"T04_NUM_ORDEM\"
           ,\"T04_NUM_REGIAO\"
           ,\"T04_DESC_UNIDADE\"
           ,\"T04_SIGLA_UNIDADE\"
           ,\"T04_NOME_CIDADE_UNIDADE\"
           ,\"T04_SIGLA_UF_UNIDADE\"
           ,\"T04_COD_NECAP\")
     VALUES
           (%s,%s,%s,%s,%s,%s,%s,%s)
"""


query_insert_t05 = """
INSERT INTO core_t05situacaouniaoprocesso
           (\"T05_ID_SITUACAO_UNIAO\"
           ,\"T05_DESC_SITUACAO_UNIAO\")
     VALUES
           (%s,%s)
"""


query_insert_t06 = """
INSERT INTO core_t06tipoparecer
           (\"T06_ID_TIPO_PARECER\"
           ,\"T06_DESC_TIPO_PARECER\")
     VALUES
           (%s,%s)
"""


query_insert_t07 = """
INSERT INTO core_t07objetoacao
           (\"T07_ID_OBJETO_ACAO\"
           ,\"T07_DESC_OBJETO_ACAO\"
           ,\"T07_NUM_GRUPO\")
     VALUES
           (%s,%s,%s)
"""


query_insert_t08 = """
INSERT INTO core_t08orgaorepresentado
           (\"T08_ID_ORGAO_REPRESENTADO\"
           ,\"T08_DESC_ORGAO_REPRESENTADO\"
           ,\"T08_COD_ORGAO_VINCULADO\"
           ,\"T08_SIGLA_ABRANGENCIA_DEMANDA\")
     VALUES
           (%s,%s,%s,%s)
"""


query_insert_t09 = """
INSERT INTO core_t09necap
           (\"T09_ID_NECAP\"
           ,\"T09_DESC_NECAP\"
           ,\"T09_COD_SENHA\"
           ,\"T09_COD_NECAP_REGIONAL\"
           ,\"T09_COD_ABRANGENCIA_ATUACAO\")
     VALUES
           (%s,%s,%s,%s,%s)
"""


query_insert_t10 = """
INSERT INTO core_t10receitaefetiva
           (\"T10_ANO_RECEITA_EFETIVA\"
           ,\"T10_MES_RECEITA_EFETIVA\"
           ,\"T10_COD_TIPO_RECOLHIMENTO\"
           ,\"T10_VR_INDENIZACAO\"
           ,\"T10_VR_HONORARIO\")
     VALUES
           (%s,%s,%s,%s,%s)
"""

query_insert_t11 = """
INSERT INTO core_t11quantidadehistorica
           (\"T11_NUM_ANO\"          
           ,\"T11_QTD_PROCESSO_ANALISADO\"
           ,\"T11_QTD_EXEQUENTE\")
     VALUES
           (%s,%s,%s)
"""


query_insert_t12 = """ 


INSERT INTO core_t12sugestaoresposta
           (\"T12_ID_SUGESTAO\"
           ,\"T12_COD_NECAP\"
           ,\"T12_NOME_SERVIDOR\"
           ,\"T12_DT_SUGESTAO\"
           ,\"T12_DESC_SUGESTAO\"
           ,\"T12_DESC_RESPOSTA\")
     VALUES
           (%s,%s,%s,%s,%s,%s)
"""


query_insert_t13 = """
INSERT INTO core_t13financeiroacordo
           (\"T13_COD_NECAP\"
           ,\"T13_NUM_PROCESSO\"
           ,\"T13_MES_ANO\"
           ,\"T13_NUM_VARA\"
           ,\"T13_NOME_AUTOR\"
           ,\"T13_VR_PRINCIPAL\"
           ,\"T13_VR_JUROS_MORA\"
           ,\"T13_VR_PGTO_ADM\"
           ,\"T13_PERC_DESCONTO\"
           ,\"T13_DT_ENTRADA_DADOS\")
     VALUES
           (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
"""


query_insert_t14 = """
INSERT INTO core_t14responsavelprocesso
           (\"T14_COD_NECAP\"
           ,\"T14_NOME_RESPONSAVEL\")
     VALUES
           (%s,%s)
"""


query_insert_t15 = """ 
INSERT INTO core_t15perito
           (\"T15_ID_PERITO\"
           ,\"T15_NOME_PERITO\"
           ,\"T15_COD_FORMACAO_PERITO\"
           ,\"T15_COD_TIPO_ATUACAO_PERITO\"
           ,\"T15_NUM_TELEFONE_PERITO\"
           ,\"T15_DESC_ORGAO_REGISTRO_PERITO\"
           ,\"T15_NUM_REGISTRO_ORGAO\"
           ,\"T15_ENDERECO_RESIDENCIA_PERITO\"
           ,\"T15_CIDADE_RESIDENCIA_PERITO\"
           ,\"T15_UF_RESIDENCIA_PERITO\")
     VALUES
           (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
"""


query_insert_t16 = """  
INSERT INTO core_t16formacaoperito
           (\"16_ID_FORMACAO_PERITO\"
           ,\"16_DESC_FORMACAO_PERITO\")
     VALUES
           (%s,%s)
"""


query_insert_t17 = """
INSERT INTO core_t17posicaoaguprocesso
           (\"T17_ID_POSICAO_AGU_PROCESSO\"
           ,\"T17_DESC_POSICAO_AGU_PROCESSO\")
     VALUES
           (%s,%s)
"""


query_insert_t18 = """
INSERT INTO core_t18propostaperito
           (\"T18_ID_PROPOSTA_HONORARIO_PERICIA\"
           ,\"T18_COD_PERITO\"
           ,\"T18_COD_PROCESSO\"
           ,\"T18_DT_PROPOSTA_PERITO\"
           ,\"T18_DESC_ASSUNTO\"
           ,\"T18_VR_PEDIDO_PERITO\"
           ,\"T18_VR_AGU\"
           ,\"T18_DT_PARECER\"
           ,\"T18_COD_POSICAO_AGU_PROCESSO\"
           ,\"T18_OBSERVACAO\")
     VALUES
           (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
"""


query_insert_t19 = """
INSERT INTO core_t19tiporecolhimentoreceita
           (\"T19_ID_TIPO_RECOLHIMENTO_RECEITA\"
           ,\"T19_DESC_TIPO_RECOLHIMENTO_RECEITA\")
     VALUES
           (%s,%s)
"""


query_insert_t20 = """
INSERT INTO core_t20tipoatuacaoperito
           (\"T20_ID_TIPO_ATUACAO_PERITO\"
           ,\"T20_DESC_TIPO_ATUACAO_PERITO\")
     VALUES
           (%s,%s)
"""


query_insert_t21 = """
INSERT INTO core_t21combinacaopossivelprocesso
           (\"T21_NUM_IDENTIFICACAO\"
           ,\"T21_COD_SITUACAO_UNIAO\"
           ,\"T21_SN_PERICIA\"
           ,\"T21_COD_TIPO_CALCULO\"
           ,\"T21_COD_OBJETO_ACAO\"
           ,\"T21_DT_CADASTRAMENTO\")
     VALUES
           (%s,%s,%s,%s,%s,%s)
"""


viewv36 = """
CREATE VIEW V36_QTD_PROCESSO_EXEQUENTE_RESPONSAVEL
AS
SELECT  
      "T09_COD_NECAP_REGIONAL" as V36_COD_NECAP_REGIONAL,
      "T04_COD_NECAP" as V36_COD_NECAP,
      EXTRACT(YEAR FROM "T01_DT_SAIDA_NECAP") as V36_ANO,
      "T01_NOME_RESPONSAVEL" as V36_NOME_RESPONSAVEL, 
      SUM("T01_QTD_EXEQUENTE") as V36_QTD_EXEQUENTE, 
      COUNT("T01_ID_PROCESSO") as V36_QTD_PROCESSO 

FROM   core_t01processo INNER JOIN core_t04origemprocesso ON
                "T01_COD_UNIDADE" = "T04_ID_UNIDADE"
                 LEFT JOIN core_t09necap ON
                 "T04_COD_NECAP" = "T09_ID_NECAP"

GROUP BY "T09_COD_NECAP_REGIONAL", EXTRACT(YEAR FROM "T01_DT_SAIDA_NECAP"), "T01_NOME_RESPONSAVEL", "T04_COD_NECAP"

HAVING ("T01_NOME_RESPONSAVEL" <> 'DECAP') AND (EXTRACT(YEAR FROM "T01_DT_SAIDA_NECAP") >= 2005)

ORDER BY EXTRACT(YEAR FROM "T01_DT_SAIDA_NECAP")
""" 


viewv18 = """
CREATE VIEW V18_QTD_PROCESSO_UNIDADE
AS
SELECT    
                    "T01_COD_UNIDADE" as V18_COD_UNIDADE,
                     EXTRACT(YEAR FROM("T01_DT_SAIDA_NECAP")) as V18_ANO_SAIDA_NECAP, 
                     EXTRACT(MONTH FROM("T01_DT_SAIDA_NECAP")) as V18_MES_SAIDA_NECAP, 
                     COUNT("T01_NUM_PROCESSO") as V18_QTD_PROCESSO
           
FROM  core_t01processo
GROUP BY "T01_COD_UNIDADE", EXTRACT(YEAR FROM("T01_DT_SAIDA_NECAP")),EXTRACT(MONTH FROM("T01_DT_SAIDA_NECAP"))
ORDER BY "T01_COD_UNIDADE", EXTRACT(YEAR FROM("T01_DT_SAIDA_NECAP")), EXTRACT(MONTH FROM("T01_DT_SAIDA_NECAP"))


"""



viewv32 = """
CREATE VIEW V32_QTD_POR_UF_DETERMINADO_PERIODO
AS
SELECT             
"T09_COD_NECAP_REGIONAL" as V32_COD_NECAP_REGIONAL, 
"T04_SIGLA_UF_UNIDADE" as V32_UF_PESQUISADA, 
"T04_COD_NECAP" as V32_COD_NECAP,
EXTRACT(YEAR FROM("T01_DT_SAIDA_NECAP")) as V32_ANO_PESQUISA, 
"T01_NOME_RESPONSAVEL" as V32_NOME_RESPONSAVEL,

CASE WHEN  EXTRACT(MONTH FROM("T01_DT_SAIDA_NECAP")) = 1 THEN COUNT("T01_ID_PROCESSO")
     ELSE 0 
END
AS V32_JAN_PESQUISADO,

CASE WHEN  EXTRACT(MONTH FROM("T01_DT_SAIDA_NECAP")) = 2 THEN COUNT("T01_ID_PROCESSO")
     ELSE 0 
END
AS V32_FEV_PESQUISADO,

CASE WHEN  EXTRACT(MONTH FROM("T01_DT_SAIDA_NECAP")) = 3 THEN COUNT("T01_ID_PROCESSO")
     ELSE 0 
END
AS V32_MAR_PESQUISADO,

CASE WHEN  EXTRACT(MONTH FROM("T01_DT_SAIDA_NECAP")) = 4 THEN COUNT("T01_ID_PROCESSO")
     ELSE 0 
END
AS V32_ABR_PESQUISADO,

CASE WHEN  EXTRACT(MONTH FROM("T01_DT_SAIDA_NECAP")) = 5 THEN COUNT("T01_ID_PROCESSO")
     ELSE 0 
END
AS V32_MAI_PESQUISADO,

CASE WHEN  EXTRACT(MONTH FROM("T01_DT_SAIDA_NECAP")) = 6 THEN COUNT("T01_ID_PROCESSO")
     ELSE 0 
END
AS V32_JUN_PESQUISADO,

CASE WHEN  EXTRACT(MONTH FROM("T01_DT_SAIDA_NECAP")) = 7 THEN COUNT("T01_ID_PROCESSO")
     ELSE 0 
END
AS V32_JUL_PESQUISADO,

CASE WHEN  EXTRACT(MONTH FROM("T01_DT_SAIDA_NECAP")) = 8 THEN COUNT("T01_ID_PROCESSO")
     ELSE 0 
END
AS V32_AGO_PESQUISADO,


CASE WHEN  EXTRACT(MONTH FROM("T01_DT_SAIDA_NECAP")) = 9 THEN COUNT("T01_ID_PROCESSO")
     ELSE 0 
END
AS V32_SET_PESQUISADO,

CASE WHEN  EXTRACT(MONTH FROM("T01_DT_SAIDA_NECAP")) = 10 THEN COUNT("T01_ID_PROCESSO")
     ELSE 0 
END
AS V32_OUT_PESQUISADO,

CASE WHEN  EXTRACT(MONTH FROM("T01_DT_SAIDA_NECAP")) = 11 THEN COUNT("T01_ID_PROCESSO")
     ELSE 0 
END
AS V32_NOV_PESQUISADO,

CASE WHEN  EXTRACT(MONTH FROM("T01_DT_SAIDA_NECAP")) = 12 THEN COUNT("T01_ID_PROCESSO")
     ELSE 0 
END
AS V32_DEZ_PESQUISADO

FROM  core_t01processo INNER JOIN core_t04origemprocesso ON 
      "T01_COD_UNIDADE" = "T04_ID_UNIDADE"
       LEFT JOIN core_t09necap ON
       "T04_COD_NECAP" = "T09_ID_NECAP"
            
WHERE  EXTRACT(YEAR FROM("T01_DT_SAIDA_NECAP")) IS NOT NULL  AND
     EXTRACT(YEAR FROM("T01_DT_SAIDA_NECAP")) <= EXTRACT(YEAR FROM(CURRENT_DATE)) 

GROUP BY   "T09_COD_NECAP_REGIONAL", 
       "T04_SIGLA_UF_UNIDADE", 
       "T04_COD_NECAP", 
       EXTRACT(YEAR FROM("T01_DT_SAIDA_NECAP")), 
       EXTRACT(MONTH FROM("T01_DT_SAIDA_NECAP")), 
       "T01_NOME_RESPONSAVEL"
         
ORDER BY   EXTRACT(YEAR FROM("T01_DT_SAIDA_NECAP")), 
       EXTRACT(MONTH FROM("T01_DT_SAIDA_NECAP")), 
       "T01_NOME_RESPONSAVEL"

"""



viewv54 = """
CREATE VIEW V54_CONSOLIDA_QTD_PROC_UF_POR_MES_RESP
AS
SELECT     
     "v32_cod_necap_regional" AS V54_COD_NECAP_REGIONAL, 
     "v32_ano_pesquisa" AS V54_ANO_PESQUISA, 
     "v32_uf_pesquisada" AS V54_UF_PESQUISADA,
     "v32_cod_necap" AS V54_COD_NECAP, 
     "v32_nome_responsavel" AS V54_NOME_RESPONSAVEL,
     SUM("v32_jan_pesquisado") AS V54_JAN_PESQUISADO, 
     SUM("v32_fev_pesquisado") AS V54_FEV_PESQUISADO,
     SUM("v32_mar_pesquisado") AS V54_MAR_PESQUISADO,
     SUM("v32_abr_pesquisado") AS V54_ABR_PESQUISADO,
     SUM("v32_mai_pesquisado") AS V54_MAI_PESQUISADO,
     SUM("v32_jun_pesquisado") AS V54_JUN_PESQUISADO, 
     SUM("v32_jul_pesquisado") AS V54_JUL_PESQUISADO,
     SUM("v32_ago_pesquisado") AS V54_AGO_PESQUISADO,
     SUM("v32_set_pesquisado") AS V54_SET_PESQUISADO,
     SUM("v32_out_pesquisado") AS V54_OUT_PESQUISADO, 
     SUM("v32_nov_pesquisado") AS V54_NOV_PESQUISADO, 
     SUM("v32_dez_pesquisado") AS V54_DEZ_PESQUISADO, 
     SUM("v32_jan_pesquisado" + "v32_fev_pesquisado" + "v32_mar_pesquisado" + "v32_abr_pesquisado" + "v32_mai_pesquisado" + "v32_jun_pesquisado" + "v32_jul_pesquisado"
     + "v32_ago_pesquisado" + "v32_set_pesquisado" + "v32_out_pesquisado" + "v32_nov_pesquisado" + "v32_dez_pesquisado") AS V54_TOTAL_UF, 
     EXTRACT(MONTH FROM(CURRENT_DATE)) - 1  AS V54_MES_LIMITE  

FROM v32_qtd_por_uf_determinado_periodo
GROUP BY "v32_cod_necap_regional", "v32_uf_pesquisada", "v32_cod_necap", "v32_ano_pesquisa", "v32_nome_responsavel"
ORDER BY "v32_uf_pesquisada", "v32_nome_responsavel"


"""



viewvx8 = """

"""



viewvx8 = """

"""