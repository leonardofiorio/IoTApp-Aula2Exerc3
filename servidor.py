# -*- coding: utf-8 -*-
from coapthon.resources.resource import Resource
from coapthon.server.coap import CoAP
import sys
from threading import Thread
from sense_emu import SenseHat
import time

# Classe para o recurso do servidor referente ao limite de temperatura
class LimTemperatura(Resource):
    def __init__(self, name="LimTemperatura", coap_server=None):
        super(LimTemperatura, self).__init__(name, coap_server, visible=True,
                                            observable=True, allow_children=True)
        self.payload = "LimTemperatura"
        self.servidor_coap = None

    def render_GET(self, request):
        return self

    def render_POST(self, request):
        # Atualizando valor de limite no servidor
        self.servidor_coap.set_limtemperatura(float(request.payload))
        res = self.init_resource(request, LimTemperatura())
        res.set_servidor_coap(self.servidor_coap)
        return res

    def set_servidor_coap(self, servidor_coap):
        self.servidor_coap = servidor_coap

    def get_servidor_coap(self):
        return self.servidor_coap

# Classe para o rescurso do servidor referente ao limite da pressão
class LimPressao(Resource):
    def __init__(self, name="LimPressao", coap_server=None):
        super(LimPressao, self).__init__(name, coap_server, visible=True,
                                            observable=True, allow_children=True)
        self.payload = "LimPressao"
        self.servidor_coap = None

    def render_GET(self, request):
        return self

    def render_POST(self, request):
        # Atualizando valor de limite no servidor
        self.servidor_coap.set_limpressao(float(request.payload))
        res = self.init_resource(request, LimPressao())
        res.set_servidor_coap(self.servidor_coap)
        return res

    def set_servidor_coap(self, servidor_coap):
        self.servidor_coap = servidor_coap
    
    def get_servidor_coap(self):
        return self.servidor_coap


class CoAPServer(CoAP):
    def __init__(self, host, port, multicast=False):
        CoAP.__init__(self, (host, port), multicast)
        print("Servidor em execução!")

        # Adicionando recurso de temperatura limite ao servidor
        rec_limtemperatura = LimTemperatura() 
        if self.add_resource("limtemperatura", rec_limtemperatura):
            rec_limtemperatura.set_servidor_coap(self)
            print("Recurso de limite de temperatura adicionado com sucesso!")

        # Adicionando recurso de temperatura limite ao servidor
        rec_limpressao = LimPressao() 
        if self.add_resource("limpressao", rec_limpressao):
            rec_limpressao.set_servidor_coap(self)
            print("Recurso de limite de pressão adicionado com sucesso!")

        # Iniciando as variáveis 
        self.limtemperatura = 130
        self.limpressao = 1300

    def set_limtemperatura(self, value):
        self.limtemperatura = value

    def set_limpressao(self, value):
        self.limpressao = value

# Função para que o servidor ouvir novos thresholds dos clientes
def ouvir_clientes(servidor):
    try:
        print("O servidor está pronto!")
        servidor.listen(10)
    except:
        print(servidor.root.dump())
        servidor.close()
        sys.exit()


if __name__=="__main__":
    # Iniciando o sensor do SenseHat
    sensor = SenseHat()

    ip_servidor = sys.argv[1]                               # Recebendo ip que o servidor ira operar
    porta_servidor = int(sys.argv[2])                       # Recebendo a porta do servidor irá operar
    servidor = CoAPServer(ip_servidor, porta_servidor)      # iniciando o servidor no ip e porta informados como parâmetro
    rgb_vermelho = (255, 0, 0)                              # Setando o rgb da cor vermelha


    # Iniciando threads para possibilitar que os clientes sejam ouvidos
    # e o senseHat seja usado simultaneamente
    thread = Thread(target = ouvir_clientes, args=(servidor,))      
    thread.setDaemon(True)
    thread.start()
    
    while True:
        # Capturando informações de pressão e temperatura informados no sensor
        pressao_atual = sensor.get_pressure()
        temperatura_atual = sensor.get_temperature()

        print("Limite de temperatura " + str(servidor.limtemperatura))
        print("Limite de pressao " + str(servidor.limpressao))

        # Teste para acender ou apagar os leds
        if temperatura_atual > servidor.limtemperatura and pressao_atual > servidor.limpressao:
            # Acende o led na cor vermelha
            pixels = [rgb_vermelho for i in range(64)]      # Configurando a cor vermelha para cada um dos 64 leds
            sensor.set_pixels(pixels)
        else:
            # Apagando os leds
            sensor.clear()