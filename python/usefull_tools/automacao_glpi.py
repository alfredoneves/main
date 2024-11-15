import requests
import json
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager    # webdriver para poder usar o google chrome na automação
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from getpass import getpass
# pip install selenium
# pip install webdriver-manager

# materiais de apoio
# https://www.youtube.com/watch?v=zH15eucEGJ8&t=2s
# https://learn.microsoft.com/pt-br/microsoftteams/platform/webhooks-and-connectors/how-to/add-incoming-webhook?tabs=newteams%2Cdotnet

ID = 139428 # último ID de ticket lançado
print("Forneça as credenciais para se autenticar no GLPI")
usuario = input("Usuário: ")
senha = getpass("Senha: ")

# webhooks
windows = ""
linux = ""
dba = ""
virt = ""
sap = ""
bkp = ""

def automacao_glpi(ID):
    global usuario
    global senha
    #servico = Service(ChromeDriverManager().install())  # instala o driver correspondente a versão atual do google
    #navegador = webdriver.Chrome(service=servico)  # cria o navegador
    try:
        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new")

        navegador = webdriver.Chrome(options=options)
        navegador.get("http://itsm.grupolight.local/index.php")

        navegador.find_element("xpath",
                                '//*[@id="login_name"]').send_keys(usuario) # username
        navegador.find_element("xpath",
                                '//*[@id="login_password"]').send_keys(senha) # senha 
        navegador.find_element("xpath", '//*[@id="boxlogin"]/form/p[5]/input').click() # enviar
    except:
        print("Erro para logar")
        return False

    print(f"Pegando ticket ID: {ID}")
    try:
        navegador.get(f'http://itsm.grupolight.local/front/ticket.form.php?id={ID}')

        navegador.implicitly_wait(10)  # Waits up to 10 seconds for elements to be found
        ticket_number_element = navegador.find_element(By.CLASS_NAME, "b_right")
        title_element = navegador.find_element(By.CLASS_NAME, "title")
        rich_text_element = navegador.find_element(By.CLASS_NAME, "rich_text_container")

        # Get the text from each element
        ticket_number = ticket_number_element.text
        title = title_element.text
        rich_text = rich_text_element.text
        ticket_completo = ticket_number + title + rich_text

        navegador.quit()
        return ticket_completo
    except:
        print("ID não encontrado")
        return False

    

def envia_mensagem_teams(titulo, mensagem, webhook): # código para apenas enviar uma mensagem via teams
    # Webhook URL from the Microsoft Teams Incoming Webhook
    try:
        webhook_url = webhook

        # Message to be sent
        message = {
            "title": titulo,
            "text": mensagem
        }

        # Send the message to the Teams channel via the webhook
        response = requests.post(
            webhook_url,
            headers={'Content-Type': 'application/json'},
            data=json.dumps(message)
        )

        # Check the response
        if response.status_code == 200:
            print("Message sent successfully.")
        else:
            print(f"Failed to send message. Status code: {response.status_code}, Response: {response.text}")
    except:
        print("Erro ao enviar mensagem no teams")

while True:
    dados = automacao_glpi(ID) # se o ID ainda não existir retorna False

    if not dados or "Solved problem:" in dados:
        sleep(30)
        pass
    else:
        ID += 1 # passa para o próximo ID

        # criar ifs para os webhooks
        if "MK-WIN" in dados:
            envia_mensagem_teams(dados[:14], dados[15:], windows)
        elif "MK-LNX" in dados:
            envia_mensagem_teams(dados[:14], dados[15:], linux)
        elif "MK-VRT" in dados:
            envia_mensagem_teams(dados[:14], dados[15:], virt)
        elif "MK-SAP" in dados:
            envia_mensagem_teams(dados[:14], dados[15:], sap)
        elif "MK-DBA" in dados:
            envia_mensagem_teams(dados[:14], dados[15:], dba)
        elif "MK-BKP" in dados:
            envia_mensagem_teams(dados[:14], dados[15:], bkp)

