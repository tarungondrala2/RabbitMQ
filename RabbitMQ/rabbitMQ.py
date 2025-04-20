import pika
import pika.credentials

def EstablishConnection():
    credentials = pika.PlainCredentials('test','test')
    connection_parameters = pika.ConnectionParameters(host='hostname',port=5672, credentials=credentials)
    connection = pika.BlockingConnection(connection_parameters)
    return connection

def InitChannel(connection) :
    channel = connection.channel()
    return channel