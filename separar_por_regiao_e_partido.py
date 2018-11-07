import pandas as pd 
import os, sys, re, locale

arquivos = sys.argv[1:]

REGIOES = 	{"nordeste":
["MA",
"PI",
"CE",
"RN",
"BA",
"PE",
"SE",
"PB",
"AL"],

"norte":["AC",
"AM",
"AP",
"PA",
"TO",
"RR",
"RO"],

"centro-oeste":["MT",
"MS",
"GO"],

"sudeste":["SP",
"RJ",
"MG",
"ES"],

"sul":["PR",
"SC",
"RS"]
}

for arquivo in arquivos:			#itera todos os arquivos passados como argumento (ou apenas um)
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
	del df
	partidos = list(df_colunas_filtradas['sgPartido'].unique())
	o = open("gastos_por_regiao_por_partido.txt","w+")
	p = '\n'
	t = '\t'
	pt = p+t
	for regiao in REGIOES.keys():
		o.write(p + "Região " + regiao + pt)
		for partido in partidos:
			print('partido: ' + str(partido))
			df_por_partido_e_regiao = df_colunas_filtradas[
				(df_colunas_filtradas['sgPartido'] == partido) & (df_colunas_filtradas['sgUF'].isin(REGIOES[regiao]))
			]
			total_deputados_regiao = len(df_por_partido_e_regiao['txNomeParlamentar'].unique())
			print(total_deputados_regiao)
			if(total_deputados_regiao == 0):		#gambiarra, tem como ser melhor
				continue
			o.write(pt+"Partido " + partido + pt)
			o.write("N. total de deputados na região: " + str(total_deputados_regiao) + pt)
			coluna_vlrDocumento = pd.to_numeric(df_por_partido_e_regiao['vlrDocumento'].str.replace(',','.'))		#"limpa" valores pra poderem ser convertidos pra float
			df_por_partido_e_regiao.update(coluna_vlrDocumento)
			gastos_totais = round(df_por_partido_e_regiao['vlrDocumento'].sum(),2)		#pega gastos totais do partido na região
			o.write("Gastos totais do partido " + partido + " na região " + regiao + ": " + str(gastos_totais) + pt)		#TODO FAZER POR ANO
			gastos_por_candidato = round(gastos_totais/float(total_deputados_regiao),2)		#pega relação de gastos/deputados
			o.write("Relação gastos/candidato: " + str(gastos_por_candidato) + pt + p)
	o.close()

	"""for partido in partidos_SC: 
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
					"""	