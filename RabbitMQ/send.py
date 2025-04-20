import pika
import pika.credentials
from rabbitMQ import EstablishConnection, InitChannel

rmq_connection = EstablishConnection()
channel = InitChannel(rmq_connection)


channel.queue_declare(queue='test_hello')                                   # creating a new queue, message sent without key will be dropped by rabbitMq

channel.basic_publish(exchange='',                                          # here we are using defualt exchange
                      routing_key='test_hello',                             # routing_key is nothing but queue created
                      body='Test Message: Hello! from pika clinet, message count: 3') 

print('[info] *** message sent ***')

rmq_connection.close()                                          # Closing connection to make sure that network buffers are flushed and our message was actually delivered to RabbitMQ
