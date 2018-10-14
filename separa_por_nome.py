# -*- coding=utf-8 -*-
"""
script para separar, por ordem alfabetica do primeiro nome, os arquivos de dados do congresso em pequenos arquivos q contem apenas politicos cujos primeiros 
nomes comecam com a letra fornecida, separados tb por ano. 
"""

import pandas as pd
import os, re, pprint
LETRAS = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","X","Y","W","Z"]
COLUNA_NOME = "txNomeParlamentar"
print("Forneça o caminho até os arquivos .csv (string do caminho relativo ou absoluto):")
caminho_arquivos = input()		#se estiver usando Python 2.x, o nome da funcao eh raw_input
print()
os.chdir(caminho_arquivos)		
arquivos_diretorio = os.listdir()

#pega apenas arquivos csv 
arquivos_csv = [arq for arq in arquivos_diretorio if arq.endswith("csv")]

#cria dicionario temporario para associar numeros aos arquivos
output_arquivos_csv = {}		
i = 1

#itera strings na lista para construir dicionario
for arquivo in arquivos_csv:
	output_arquivos_csv[i] = arquivo
	i += 1 

#apresenta para o usuario	
print("Em qual arquivo deseja que seja feita a separação por nomes em ordem alfabética (forneça o número correspondente ao arquivo)?")
pprint.pprint(output_arquivos_csv)

#colhe input do usuario, com tratamento de excecao
inp = None 
while(not inp):
	try:
		inp = int(input())
	except ValueError:
		print("Forneça um número")

#pega o arquivo associado ao numero fornecido
arquivo_csv_alvo = output_arquivos_csv[inp]	

#despeja dicionario por nao ser mais util para economia de memoria	
del output_arquivos_csv

#colhe o ano do arquivo
padrao = re.compile("[0-9]{4}")
ano = padrao.findall(arquivo_csv_alvo)[0]

#cria uma pasta distinta para colocar os arquivos e muda o caminho para ela 
nome_pasta = "nomes_politicos_" + ano
caminho_pasta = os.path.join(os.getcwd(),nome_pasta)
os.mkdir(nome_pasta)				
os.chdir(caminho_pasta)

#delimiter=; estah hard-coded pq os arquivos com os quais isso foi escrito em mente possuem esse delimitador
dataframe_arquivo = pd.read_csv("../"+arquivo_csv_alvo,delimiter=";")		#gambiarra... nao me julgue...

#itera as letras e separa todos os politicos cujos nomes comecam com a letra atual no arquivo alvo 
#cria arquivos dentro da pasta criada
print("Criando arquivos na pasta: " + nome_pasta)
print("No diretório: " + caminho_pasta)
print()
for letra in LETRAS:
	nome_arquivo_novo = "politicos_" + letra + "_" + ano + ".csv"
	arquivo_novo = open(nome_arquivo_novo,"w")
	print("Processando nomes que começam com " + letra + "...")
	print("Armazenando resultados no arquivo: " + nome_arquivo_novo)
	dataframe_novo = dataframe_arquivo[dataframe_arquivo[COLUNA_NOME].str.startswith(letra)]
	dataframe_novo.to_csv(arquivo_novo,sep=";",encoding="utf-8",header=True)
	arquivo_novo.close()
	print("Processamento de nomes que começam com " + letra + " concluído.")
	print()

