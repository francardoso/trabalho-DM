import pandas as pd
import requests
import json, csv
import os, sys
from time import sleep

file_cnpjs = 'respostas_receita_cnpjs.csv'
file_ceapd = 'ceapd_2017.csv'
url = 'https://www.receitaws.com.br/v1/cnpj/:cnpj'
data = None
sleep_secs = 10
CAMPOS_INTERESSE = ['cnpj','nome','fantasia','uf','atividade_principal','uf','municipio','cep','abertura','situacao']

# Cria arquivo de CNPJs únicos ou lê caso já exista
if os.path.isfile(file_cnpjs):
	data = pd.read_csv(file_cnpjs, dtype = str)
	cnpjs = list(data['txtCNPJCPF'].unique())
elif os.path.isfile(file_ceapd):
	data = pd.read_csv(file_ceapd, sep = ';', dtype = str)
	cnpjs = list(data['txtCNPJCPF'].unique())

with open(file_cnpjs,"w+") as arq_csv:
	escritor = csv.DictWriter(arq_csv,fieldnames=CAMPOS_INTERESSE,delimiter=";")
	escritor.writeheader()
	for cnpj in cnpjs: 
		r = requests.get(url.replace(':cnpj', str(cnpj)))
		while r.status_code != 200:
			print('Bad request: ' + r.text)
			print('Sleeping for ' + str(sleep_secs) + ' seconds...')
			sleep(sleep_secs)			
			r = requests.get(url.replace(':cnpj', str(cnpj)))
		
		cnt = r.json()
		cnt_2 = {k: cnt[k] for k in CAMPOS_INTERESSE}			#remove tuplas irrelevantes (JSON de resposta vem com tuplas a mais)
		bytess = escritor.writerow(cnt_2)
		print("escreveu " + str(bytess) + " no arquivo")