#!/usr/bin/python3

import datetime
from playsound import playsound
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from time import sleep

# configuração para web scraping 
option = webdriver.ChromeOptions()
option.add_argument('headless')
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico, options=option)


def pega_parametros():
	global max_fila
	global max_tme
	global max_tma
	
	while True:
		try:
			print("Valores sugeridos:\n2 usuários em fila\nTME = 9\nTMA = 9")
			max_fila = int(input("Digite o máximo de usuários limite da fila: "))
			max_tme = int(input("Digite o máximo de TME: "))
			max_tma = int(input("Digite o máximo de TMA: "))
			break
		except Exception as error:
			print(error)

	
def time_stamp():
	t = datetime.datetime.now()
	return f"{t.day}/{t.month}/{t.year} - {t.hour}:{t.minute}:{t.second}"
	

def logar():
	with open("logs.txt", "a") as my_file:
		my_file.write(f"{t} : {tme} : {tma} : {fila}\n")
		
		
# função para extrair dados da web
def extrair_dados():
	global tme
	global tma
	global fila
	global t
	
	print("---" * 20)
	t = time_stamp()
	print(f"Analisando... {t}")
	
	navegador.get("URL DO DASHBOARD")
	sleep(5)

	tme = navegador.find_element('xpath', '//*[@id="root"]/div/div/main/div/div/div[2]/div/div/div[6]/div/div/div/div/div[2]/span/h1').text
	print(f"TME: {tme}")

	tma = navegador.find_element('xpath', '//*[@id="root"]/div/div/main/div/div/div[2]/div/div/div[7]/div/div/div/div/div[2]/span/h1').text
	print(f"TMA: {tma}")

	fila = navegador.find_element('xpath', '//*[@id="root"]/div/div/main/div/div/div[2]/div/div/div[4]/div/div/div/div/div[2]/span/h1').text
	print(f"Usuários em fila: {fila}")


	
pega_parametros()	# define os valores máximos para gerar o alerta

while True:
	extrair_dados()
	logar()
	try:
		if int(tme[6:8]) >= max_tme or int(fila) >= max_fila or int(tma[3:5]) >= max_tma:
			playsound('alerta.mp4', True)	# soa o alerta
		else:
			print("SLA OK")
	except Exception as error:
		print(error)
		
	sleep(20)
