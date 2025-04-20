import pika
import sys
import os
from rabbitMQ import EstablishConnection, InitChannel



def main():
    rmq_connection = EstablishConnection()
    channel = InitChannel(connection=rmq_connection)

    channel.queue_declare('test_hello')

    '''
    Receiving messages from the queue is more complex. 
    It works by subscribing a callback function to a queue. 
    Whenever we receive a message, this callback function is called by the Pika library. 
    In our case this function will print on the screen the contents of the message.
    '''
    def callback(ch, method, properties, body):
        print(f"[out] recieved: {body}")

    channel.basic_consume(queue='test_hello',
                          auto_ack=True,
                          on_message_callback=callback)
    
    print(' [IMP] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
    

if __name__ == '__main__' :
    try:
        main()
    except KeyboardInterrupt:
        print('[ERR] user interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)


