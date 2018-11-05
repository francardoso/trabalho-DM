import pandas as pd 
import os, sys, re, locale

arquivos = sys.argv[1:]

for arquivo in arquivos:
	#colhe o ano do arquivo
	padrao = re.compile("[0-9]{4}")
	ano = padrao.findall(arquivo)[0]
	nome_pasta = "partidos_SC_" + ano
	caminho_pasta = os.path.join(os.getcwd(),nome_pasta)
	os.mkdir(nome_pasta)				

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

	df_politicos_SC = df_colunas_filtradas[df_colunas_filtradas['sgUF'] == 'SC']
	partidos_SC = list(df_politicos_SC['sgPartido'].unique())
	print("Criando arquivos na pasta: " + nome_pasta)
	print("No diretório: " + caminho_pasta)
	print()

	for partido in partidos_SC: 
		nome_arquivo_novo = "politicos_partido_" + partido + "_" + ano + ".csv"
		arquivo_novo = open(os.path.join(nome_pasta,nome_arquivo_novo),"w")
		print("Processando candidatos no estado de SC do partido " + str(partido) + "...")
		print("Armazenando resultados no arquivo: " + nome_arquivo_novo)
		df_novo = df_politicos_SC[df_politicos_SC['sgPartido'] == partido]
		coluna_vlrDocumento = pd.to_numeric(df_novo['vlrDocumento'].str.replace(',','.'))
		df_novo.update(coluna_vlrDocumento)
		df_novo.to_csv(arquivo_novo,sep=";",encoding="utf-8")
		arquivo_novo.close()
		print("Processamento de candidatos do partido " + partido + " completo.")
		print()