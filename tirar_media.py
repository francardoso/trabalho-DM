import pandas as pd
import os, sys
diretorio = sys.argv[1:][0]
print(sys.argv)
print(diretorio) 
arqs = os.listdir(diretorio)
soma = 0
temp = open("gastos_partidos.txt","w+")
for arquivo in arqs:
	nome_arquivo = os.path.join(diretorio,arquivo)
	print(nome_arquivo)
	df = pd.read_csv(nome_arquivo,delimiter=";",encoding="utf-8")
	print("processando arquivo " + arquivo)
	gastos_totais = round(df['vlrDocumento'].sum(),2)		#arredonda pra 2 casas decimais
	part = df.iloc[0]['sgPartido']
	linha = "gastos totais do partido " + part + " em 2017: " + str(gastos_totais) + "\n"
	temp.write(linha)
	soma += gastos_totais
media = round(soma/float(len(arqs)),2)
linha = "media dos gastos totais: " + str(media) + "\n"
temp.write(linha)
temp.close()