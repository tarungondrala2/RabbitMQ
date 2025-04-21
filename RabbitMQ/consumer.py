import sys
import os
from rabbitMQ import RabbitMQ



def main():
    rabbit_mq = RabbitMQ()
    rabbit_mq.establish_connection()
    rabbit_mq.init_channel()
    rabbit_mq.declare_new_queue(queue_name='test_hello_2')

    rabbit_mq.consume_basic_message(queue_name='test_hello_2', send_acknowledgement=True)
    
    print(' [IMP] Waiting for messages. To exit press CTRL+C')
    rabbit_mq.start_consuming()
    

if __name__ == '__main__' :
    try:
        main()
    except KeyboardInterrupt:
        print('[ERR] user interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)


