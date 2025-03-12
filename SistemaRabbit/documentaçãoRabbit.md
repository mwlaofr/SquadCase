## RabbitMQ
RabbitMQ é um Message Broker que permite a comunicação assíncrona entre aplicações desacopladas. Ele utiliza um modelo baseado em filas para armazenar mensagens até que possam ser processadas pelos consumidores

### Fila
No RabbitMQ uma fila é um buffer que armazena mensagens temporariamente até que um consumidor as processe. Seguem o modleo FIFO (First In, First Out), ou seja, as mensagens são consumidas na ordem em que foram enviadas

### Publicador
O publicador é a aplicação que envia mensagens ao RabbitMQ. Ele pode publicar diretamente ou através de um exchange, que roteia a mensagem para a fila correta

### Consumidor
O consumidor é a aplicação que lê e processa mensagens da fila. Um ou mais consumidores podem consumir mensagens da mesma fila. Se houver múltiplos consumidores, o RabbitMQ distribuirá as mensagens entre eles (load balancing).


- Um produtor pode enviar mensganes mesmo que nenhum consumidor esteja ativo no momento. As mensagens permanecerão na fila até que alguem as consuma
- Um consumidor pode ser configurado para processar mensagens automaticamente ou apenas após confirmar que a processou corretamente (usando acknowledgment)

## Exchange
O exchange é um ponto intermediário que recebe mensagens dos produtores e decide quais filas eles devem ser encaminhadas. Diferentes tipos de exchanges permitem roteamento flexível de mensagens

### 📌 Tipos de Exchange
- **Direct:** Mensagens são enviadas para filas que possuem uma routing key exata.
- **Fanout:**	Mensagens são enviadas para todas as filas vinculadas ao exchange, ignorando routing keys.
- **Topic:**	Mensagens são roteadas com base em padrões de routing keys usando * e #.
- **Headers:**	Roteamento baseado nos cabeçalhos da mensagem, não na routing key.

### Roteamento
Quando um produtor publica uma mensagem, ele deve indicar:
1. Qual exchange usar
2. Qual Routing Key aplicar
3. O conteúdo da mensagem

O Exchange então decide para quais filas encaminhar a mensagem com base no seu tipo e nas regras de binding.

### Binding
Um binding é a ligação entre um exchange e uma fila. Sem um binding, a mensagem enviada ao exchange não chega a nenhuma fila.\
Por exemplo, se tivermos um exchange do tipo "direct", precisamos definir uma routing key no binding para que as mensagens cheguem as filas corretas.

### Durabilidade
Para as mensgaens não serem apagadas quando o servidor reiniciar, é possível fazer dois ajustes:
- Tornar a fila durável com: ```durable= true``` Isso garante que a fila não desapareça após um reinício.
- Tornar as mensagens persistentes: ```delivery_mode=2``` Isso evita que mensagens já publicadas sejam apagadas antes do processamento.

Você pode querer ver quais filas o RabbitMQ tem e quantas mensagens estão nelas. Você pode fazer isso (como um usuário privilegiado) usando a rabbitmqctlferramenta:

```rabbitmqctl.bat list_queues```

## Filas de Trabalho
Uma fila de trabalho ou Work Queue, é usada para distribuir tarefas demoradas entre varios Workers. Sua principal ideia é evitar fazer uma tarefa que exija muitos recursos imediatamente e ter que esperar que ela seja concluida. Em vez disso, agendamos a tarefa para ser feita mais tarde, encapsulando-a como uma mensagem e enviando para a fila. Um processo de trabalho em execução em segundo plano irá estourar as tarefas e, eventualmente, executar o trabalho. Quando você executa muitos workers, as tarefas serão compartilhadas entre eles.