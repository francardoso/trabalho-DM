import pandas as pd 
import os, sys, re
import urllib.request
import xml.etree.ElementTree as ET

arquivos = sys.argv[1:]
url = "http://www.camara.leg.br/SitCamaraWS/Deputados.asmx/ObterDetalhesDeputado?ideCadastro=:idecadastro&numLegislatura="

for arquivo in arquivos:
	df = pd.read_csv(arquivo,delimiter=';',encoding='utf-8')
	groupby_mes_gastos = df.groupby(['txNomeParlamentar','idecadastro','sgPartido','sgUF','numMes'])['vlrDocumento'].agg('sum')
	nome_arquivo = arquivo.replace('csv','') + "_segmentado.csv"
	o = open(nome_arquivo,"w+")
	colunas = "txNomeParlamentar;idecadastro;sgPartido;sgUF;numMes;totalGastosMes\n"
	o.write(colunas)
	groupby_mes_gastos.to_csv(o,sep=';',encoding='utf-8')
	o.close()
	df_segmentado = pd.read_csv(nome_arquivo,delimiter=";",encoding="utf-8",dtype=str)
	df_segmentado['sexo'] = None 
	df_segmentado['numeroComissoes'] = None
	for deputado in df_segmentado['txNomeParlamentar'].unique():
		df_temp = df_segmentado[df_segmentado['txNomeParlamentar'] == deputado]
		reg = df_temp.iloc[0]
		idecadastro = str(int(float(reg.idecadastro)))
		url_deputado = url.replace(":idecadastro",idecadastro)
		print(url_deputado)
		resposta = urllib.request.urlopen(url_deputado).read()
		XML_resposta = ET.fromstring(resposta)
		deputado_XML = XML_resposta.find('Deputado')
		sexo = deputado_XML.find('sexo').text
		numero_comissoes = len(deputado_XML.find("comissoes").getchildren())
		df_temp['sexo'] = sexo
		df_temp['numeroComissoes'] = numero_comissoes
		df_segmentado.update(df_temp)
	o = open(nome_arquivo,"w+")
	df_segmentado.to_csv(o,sep=';',encoding='utf-8',index=False)
	o.close()