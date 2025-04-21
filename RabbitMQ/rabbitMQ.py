from pika import PlainCredentials, ConnectionParameters, BlockingConnection

class RabbitMQ:

    # -------------------------------- RabbitMQ Connection & Channel ---------------------------------------
    rmq_connection = None
    rmq_channel = None

    def __init__(self):
        self.HOST = '10.194.49.46'
        self.PORT_NUMBER = 5672
        self.USER_NAME = 'test'
        self.PASSWORD = 'test'
    
    def establish_connection(self):
       if self.rmq_connection is None:
            credentials = PlainCredentials(self.USER_NAME, self.PASSWORD)
            connection_parameters = ConnectionParameters(host=self.HOST,port=self.PORT_NUMBER,credentials=credentials)
            self.rmq_connection = BlockingConnection(connection_parameters)
            print('[info] Connection established successfully')

            return self.rmq_connection
       else:
           return self.rmq_connection
       
    def close_connection(self):
        self.rmq_connection.close()
        print('[info] *** Connection Closed ***')
       
    def init_channel(self):
        if self.rmq_channel is not None:
            return self.rmq_channel
        
        if self.rmq_connection is None:
            self.EstablishConnection()

        self.rmq_channel = self.rmq_connection.channel()

        return self.rmq_channel
    
    def declare_new_queue(self,queue_name):
        self.check_channel()
        self.QUEUE_NAME = queue_name
        self.rmq_channel.queue_declare(queue=self.QUEUE_NAME)
        print(f'[info] *** Declared queue: {self.QUEUE_NAME} ***')

    def check_channel(self):
        if self.rmq_channel is None:
            self.init_channel()
            return True

        return False
    
    # ---------------------------- Used by Publisher -----------------------------------------------------------
    def publish_basic_message(self, exchange, routing_key, message):
        self.check_channel()
        self.rmq_channel.basic_publish(exchange=exchange,
                                        routing_key=routing_key,
                                        body=message
        )
        print('[info] *** message sent ***')
    
    # ---------------------------- Used by Consumer ------------------------------------------------------------
    def start_consuming(self):
        self.rmq_channel.start_consuming()

    def consume_basic_message(self, queue_name, send_acknowledgement):
        print(f'[info] Trying to consume message from queue: {queue_name}')
        self.rmq_channel.basic_consume(queue=queue_name,
                                       auto_ack=True,
                                       on_message_callback=self.callback)

    '''
    Receiving messages from the queue is more complex. 
    It works by subscribing a callback function to a queue. 
    Whenever we receive a message, this callback function is called by the Pika library. 
    In our case this function will print on the screen the contents of the message.
    '''
    def callback(self, ch, method, properties, body):
        print(f"[out] recieved: {body}")

    def consume_data_from_logAggregator():
        print('[info]')