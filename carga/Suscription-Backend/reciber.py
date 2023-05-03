import pika
import mariadb
import datetime
from common import *


###############################################################################
def get_connection_db(conn):
    return mariadb.connect(user=conn["user"],
                            password=conn["pass"],
                            host=conn["host"],
                            port=conn["port"],
                            database=conn["database"])

###############################################################################

# Set up a connection to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the three queues
queue1 = 'metallica'
queue2 = 'weeknd'
queue3 = 'otros'
queue4 = 'desencolar'

counters = {
    queue1: 0,
    queue2: 0,
    queue3: 0
}

channel.queue_declare(queue=queue1)
channel.queue_declare(queue=queue2)
channel.queue_declare(queue=queue3)
channel.queue_declare(queue=queue4)

# Dequeue up to 10 messages from each queue
while True:
    for queue in [queue1, queue2, queue3, queue4]:
        if queue != "desencolar" and counters[queue] < 10:
            method, properties, body = channel.basic_get(queue=queue, auto_ack=True)
            if method:
                counters[queue] +=1
                try:
                    connection = get_connection_db(dbConnConfig["dbConnConfig"])
                    cursor = connection.cursor()

                    sqlStatement = """INSERT INTO token (Valor, Fecha) VALUES (%s, %s)"""

                    cursor.execute(sqlStatement, (body.decode(), datetime.datetime.now()))
                    connection.commit()
                    print(body.decode() + "  " + queue + "  " + str(counters[queue]))

                except (Exception, mariadb.Error) as error :
                    if(connection):
                        print("Failed insert one ", error)

                finally:
                    #closing database connection.
                    if(connection):
                        cursor.close()
                        connection.close()   
            else:
                pass
        if queue == "desencolar":
            method, properties, body = channel.basic_get(queue=queue, auto_ack=True)
            if method:
                counters[body.decode()] -= 1
            else:
                pass