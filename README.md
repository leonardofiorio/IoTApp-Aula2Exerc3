# IoTApp-Aula2Exerc3

Este projeto é apresentado a disciplina de IoT 2020-1 do curso de Mestrado em Computação da Universidade Federal Fluminense.


O exercício proposto na Aula 2 consiste em adaptar a implementação do Exercício 2 da Aula 1 para uma arquitetura cliente/servidor utilizando a comunicação CoAP. Na solução desse exercício as funcionalidades são divididas em duas camadas. A primeira camada é a do servidor responsável pelo gerenciamento do sensoriamento, atuação e disponibilização através de recursos. A segunda camada são os clientes. Os clientes podem utilizar os recursos que o servidor oferece permitindo o envio de novos valores de threshold de temperatura e pressão para o cliente através do CoAP. 


A solução é composta por um servidor. Ao ser iniciado, o servidor inicia o SenseHat com sua interface de leds e sensoriamento. Dessa forma, uma thread no servidor é responsável por coletar os valores de temperatura e pressão do sensor e comparar continuamente com as variáveis que armazenam os limites de temperatura e pressão. Por padrão, o servidor inicia com os valores de limite de 130ºC para temperatura e 1300 de pressão. Estes valores foram escolhidos pois representam valores maiores que a interface do SenseHat permite. A outra thread do servidor é responsável por receber os novos valores de threshold enviados pelos dispositivos clientes representados na camada inferior da figura. Existem dois recursos disponíveis no CoAP do servidor: limtemperatura e limpressao. Estes são os recursos utilizados pelos clientes. Os clientes, por sua vez, são compostos por uma implementação cliente do CoAP e, durante sua chamada, recebem como parâmetro os valores de thresholds de temperatura e pressão (nesta ordem) para fazerem o envio para o servidor. A figura abaixo mostra o esquema implementado.

![Alt text](esquema.png?raw=true "Title")

__Pré-requisitos__

- Python 2.7.16
- SenseHat 1.1
- CoAPthon 4.0.2

__Guia de instalação__

Os procedimentos de instalação deste guia são para sistemas Raspbian e outras distribuições baseadas em Debian.

1. Instalar o Pip
```bash
$ sudo apt install python-pip
```

2. Instalar o CoAPthon 4.0.2
```bash
$ sudo pip install CoAPthon
```

__Guia de execução__

1. Abrir o SenseHat

2. Executar o servidor informando comando de acordo com a seguinte sintaxe:
```bash
$ sudo python servidor.py <ip> <porta>
```

3. Executar o cliente informando comando de acordo com a seguinte sintaxe:
```bash
$ python cliente.py <ip> <porta> <novo limite de temperatura> <novo limite de pressão>
```
