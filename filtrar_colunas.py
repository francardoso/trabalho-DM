import pandas as pd
import sys
arquivo = sys.argv[1:][0]

df = pd.read_csv(arquivo,delimiter=";",encoding="utf-8")
df_colunas_filtradas = df[[
			'txNomeParlamentar',
			'idecadastro',
			'nuLegislatura',
			'sgUF',
			'sgPartido',
			'txtDescricaoEspecificacao',
			'txtCNPJCPF',
			'datEmissao',
			'vlrDocumento',
			'numMes'
	]]
arq_csv = open("ceapd_2017_colunas_filtradas.csv","w")
df_colunas_filtradas.to_csv(arq_csv,sep=";",encoding="utf-8")