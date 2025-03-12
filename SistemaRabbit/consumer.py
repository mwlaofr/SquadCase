import pika

#recebe e exibe os pedidos recebidos

#configurações rabbit
QUEUE_NAME = "fila_pedidos"
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue=QUEUE_NAME)

def receber_pedidos (ch, method, properties, body):
  print(f"[✔] Pedido recebido: {body.decode()}")  
  
#chama a função sempre que receber uma mensagem
channel.basic_consume(queue=QUEUE_NAME, on_message_callback=receber_pedidos, auto_ack=True)

print("Agurdando pedidos... Pressione crtl + c para sair")
channel.start_consuming()