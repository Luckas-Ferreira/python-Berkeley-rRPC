# Python gRPC Chat

Implementação do algoritmo Berkeley usando rRPC, onde as mensagens podem ser enviadas simultaneamente juntamente com o seu horario de envio. Ao receber, acrescentei um atraso de 1 minuto para todas as mensagens. Não precisa esperar receber uma mensagem para poder enviar. Use threads para implementar a concorrência. Observe que não há cliente ou servidor neste cenário, apenas partes (nós) comunicantes.

2023.2 - SISTEMAS DISTRIBUÍDOS - TURMA A

# Equipe

José Lucas Ferreira dos Santos

José Roberto da Silva 

# Instalar bibliotecas 

Pode usar o venv para criação de ambientes virtuais, que fará tudo de forma automatica, caso aconteça algum erro, instalar manualmente.

pip install grpcio

pip install grpcio-tools

pip install protobuf

pip install six
