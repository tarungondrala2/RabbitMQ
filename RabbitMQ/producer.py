from rabbitMQ import RabbitMQ

# rmq_connection = EstablishConnection()
# channel = InitChannel(rmq_connection)


# channel.queue_declare(queue='test_hello')                                   # creating a new queue, message sent without key will be dropped by rabbitMq

# channel.basic_publish(exchange='',                                          # here we are using defualt exchange
#                       routing_key='test_hello',                             # routing_key is nothing but queue created
#                       body='Test Message: Hello! from pika clinet, message count: 3') 

# print('[info] *** message sent ***')

# rmq_connection.close()                                          # Closing connection to make sure that network buffers are flushed and our message was actually delivered to RabbitMQ

rabbit_MQ = RabbitMQ()

rabbit_MQ.establish_connection()

rabbit_MQ.init_channel()

rabbit_MQ.declare_new_queue(queue_name='test_hello_2')

rabbit_MQ.publish_basic_message(exchange='',routing_key='test_hello_2',message='Test message ******')