#!/usr/bin/env python
# -*- coding: utf-8 -*-
from coapthon.client.helperclient import HelperClient
import sys

ip_servidor = sys.argv[1]           # Recebendo o ip do servidor a ser conectado
porta_servidor = int(sys.argv[2])   # Recebendo a porta do servidor
global cliente
cliente = HelperClient(server=(ip_servidor, porta_servidor))    # Criando um cliente CoaP

temperatura_lim = sys.argv[3]   # Recebendo a nova temperatura limite para ser enviada do cliente para o servidor
pressao_lim = sys.argv[4]       # Recebendo a nova pressão limite para ser enviada do cliente para o servidor

# Definindo paths no servidor
recurso_temperatura_lim = "limtemperatura"
recurso_pressao_lim = "limpressao"


try:
    # enviando a temperatura limite via POST
    response = cliente.post(recurso_temperatura_lim, temperatura_lim)
    print(response.pretty_print())
except:
    print("Deu erro no envio da temperatura limite!")


try:
    # enviando pressão limite via POST
    response = cliente.post(recurso_pressao_lim, pressao_lim)
    print(response.pretty_print())
except:
    print("Deu erro no envio da pressão limite!")

cliente.stop()