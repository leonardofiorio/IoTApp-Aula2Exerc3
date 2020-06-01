# IoTApp-Aula2Exerc3

Este projeto é apresentado a disciplina de IoT 2020-1 


__Pré-requisitos__
- Python 2.7.16
- SenseHat 1.1
- CoAPthon 4.0.2

__Guia de instalação__
Os procedimentos de instalação deste guia são para sistemas Raspbian e outras distribuições baseadas em Debian.

1. Instalar o Pip
$ sudo apt install python-pip

2. Instalar o CoAPthon 4.0.2
$ sudo pip install CoAPthon

__Guia de execução__

1. Abrir o SenseHat

2. Executar o servidor informando comando de acordo com a seguinte sintaxe:
$ sudo python servidor.py <ip> <porta>

3. Executar o cliente informando comando de acordo com a seguinte sintaxe:
$ python cliente.py <ip> <porta> <novo limite de temperatura> <novo limite de pressão>