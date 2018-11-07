import urllib.request
import xml.etree.ElementTree as ET
import csv

contents = urllib.request.urlopen("http://www.camara.gov.br/SitCamaraWS/Deputados.asmx/ObterDeputados?").read()


file = open("deputados.xml","wb") 
file.write(contents)
file.close()

tree = ET.parse("deputados.xml")
root = tree.getroot()

Deputados_data = open('Deputados.csv', 'w')

csvwriter = csv.writer(Deputados_data)
resident_head = []

count = 0
for member in root.findall('deputado'):
	deputado = []
	address_list = []
	if count == 0:
		name = member.find('nome').tag
		resident_head.append(name)
		uf = member.find('uf').tag
		resident_head.append(uf)
		EmailAddress = member.find('email').tag
		resident_head.append(EmailAddress)
		csvwriter.writerow(resident_head)
		count = count + 1

	name = member.find('nome').text
	deputado.append(name)
	uf = member.find('uf').text
	deputado.append(uf)
	EmailAddress = member.find('email').text
	deputado.append(EmailAddress)
	csvwriter.writerow(deputado)
Deputados_data.close()