import pika
import mariadb
import time
from datetime import datetime, timedelta
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
connectionQ = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connectionQ.channel()

queue = 'desencolar'

channel.queue_declare(queue=queue)


while True:
    resp=[]
    try:
        connection = get_connection_db(dbConnConfig["dbConnConfig"])
        cursor = connection.cursor()

        sqlStatement = "SELECT * FROM token WHERE Fecha <= " + str(int(time.time()))

        cursor.execute(sqlStatement)
        connection.commit()
        resp = cursor.fetchall()
        for i in resp:
            try:
                sqlStatement = 'DELETE FROM token WHERE Valor = "' + i[0] + '"'
                cursor.execute(sqlStatement)
                connection.commit()

                connectionQ = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1'))
                channel = connectionQ.channel()
                channel.basic_publish(exchange='', routing_key="desencolar", body = i[2])
                

            except (Exception, mariadb.Error) as error :
                if(connection):
                    print("Failed ", error)

    except (Exception, mariadb.Error) as error :
        if(connection):
            print("Failed ", error)

    finally:
        #closing database connection.
        if(connection):
            cursor.close()
            connection.close()

    time.sleep(10)