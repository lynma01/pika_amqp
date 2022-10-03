import pika

def hello_amqp():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    channel.basic_publish(exchange='',
                        routing_key='hello',
                        # TODO #1 - @lynma01 
                        body='Hello World!')

    print("[x] Sent 'Hello World!'")

    connection.close()

if __name__ == "__main__":
    hello_amqp()