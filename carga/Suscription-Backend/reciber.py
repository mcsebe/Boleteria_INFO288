import pika, sys, os

def main():
    conciertos = {"metallica": 0, "weeknd": 0, "otros": 0}

    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel2 = connection.channel()
    channel3 = connection.channel()

    def callback(ch, method, properties, body):
        conciertos['metallica'] += 1
        print(" [x] Received " + body.decode())
        # Nombre de la cola
        if(conciertos['metallica'] >= 100):
            channel.stop_consuming()

    def callback2(ch, method, properties, body):
        conciertos['weeknd'] += 1
        print(" [x] Received " + body.decode())
        if(conciertos['weeknd'] >= 100):
            channel2.stop_consuming()

    def callback3(ch, method, properties, body):
        conciertos['otros'] += 1
        print(" [x] Received " + body.decode())
        if(conciertos['otros'] >= 100):
            channel3.stop_consuming()

    channel.basic_consume(queue='metallica', on_message_callback=callback, auto_ack=True)
    channel2.basic_consume(queue='weeknd', on_message_callback=callback2, auto_ack=True)
    channel3.basic_consume(queue='otros', on_message_callback=callback3, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
    channel2.start_consuming()
    channel3.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)