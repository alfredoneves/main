#!/usr/bin/python3
import subprocess
from time import sleep
from datetime import datetime

def pega_hosts(arquivo):
    hosts = []
    with open(arquivo, "r") as arq:
        for host in arq.readlines():
            hosts.append(host.strip())
    return hosts

# a função abaixo terá que ser alterada para filtrar o output do ping em máquina windows
"""
command = f"ping -n1 {host} | findstr bytes="
proc
resultado
return resultado.split()[4]
"""
def pinga_host(host):
    try:
        command = f"ping -c 1 {host} | grep 'bytes from' | cut -d ' ' -f 4,7"
        proc = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE,  stdout=subprocess.PIPE, stdin=subprocess.PIPE)
        resultado =  proc.stdout.read().decode() + proc.stderr.read().decode()
        
        # se houver erro de DNS ou o host não responder o retorno será none
        if resultado == "" or "ping" in resultado:
            return "none"

        # pegando apenas o tempo de resposta do resultado
        return resultado.split()[1]    
    
    except Exception as error:
        print(f"Host: {host} error: {error}")
        return "none"

def avalia_respostas(respostas):
    for i in respostas:
        #print(f"{i}:{respostas[i]}")
        
        if respostas[i] == ["none", "none", "none"]:    # se não há resposta 3 vezes consecutivas o email é enviado
            envia_email(f"Host {i} está offline!\n{i}:{respostas[i]}")
            sleep(3)    # alterar para 120 em produção
    
    # envio de relatório
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    # remover o True abaixo em produção
    if True or ("07:00" <= current_time <= "07:03") or ("14:00" <= current_time <= "14:03") or ("22:30" <= current_time <= "22:33"):
        # preparando mesagem
        mensagem = ""

        for i in respostas:
            mensagem = mensagem + f"{i}:{respostas[i]}\n"
        envia_email(mensagem)

        sleep(1)    # alterar para 120 em produção

def envia_email(mensagem):
    print("Email enviado:") # remover em produção
    print(mensagem)
    print("-----------------")  # remover em produção

hosts = pega_hosts("hosts_importantes.txt")
contador = 0
respostas = {} # {host: [resp1, resp2, resp3]}

while True:

    for host in hosts:
        if contador == 0:
            respostas[host] = [pinga_host(host)]
        else:
            respostas[host].append(pinga_host(host))

    if contador == 2:
        avalia_respostas(respostas)
        respostas = {}
        contador = 0
        continue    # evita que o contador recebe +1 em baixo para que o if de cima seja ativado em vez do else
    
    sleep(2)    # aumentar isso para 40 quando estiver em produção (o ciclo de testes será de aproximadamente 2 minutos)
    contador+=1

