import pika

#envia os pedidos para a fila

#configurações rabbit
QUEUE_NAME = "fila_pedidos"
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

#declara fila
print("Fila criada")
channel.queue_declare(queue=QUEUE_NAME)

pedidos = ["Donut", "Bolo", "Café", "Torrada"]
for pedido in pedidos: 
  #envia o pedido 
  channel.basic_publish(exchange='', routing_key=QUEUE_NAME, body=pedido)
  print(f"[x] Pedido enviado: {pedido}")

connection.close()
