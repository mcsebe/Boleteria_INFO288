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


# Se establece la conexión con RabbitMQ
credentials = pika.PlainCredentials("user","user")
connectionQ = pika.BlockingConnection(pika.ConnectionParameters("rabbitmq",5672,'/',credentials))
channel = connectionQ.channel()

# Variables que se utilizarán
queue = 'desencolar'
format = "%H:%M:%S;%d/%m/%Y"

logW = os.getcwd() + "\\Log\\" + "logs.txt"
try:
    file = open(logW, 'a+')
except:
    logL = os.getcwd() + "/files/" + "logs.txt"
    file = open(logL, 'a+')

channel.queue_declare(queue=queue)


# Función que se ejecuta permanente mente y elimina de la base de datos los tokens expirados
while True:
    resp = []
    try:
        # Realiza una consulta a la base de datos, obteniendo los tokens expirados
        connection = get_connection_db(dbConnConfig["dbConnConfig"])
        cursor = connection.cursor()

        sqlStatement = "SELECT * FROM token WHERE Fecha <= " + \
            str(int(time.time()))

        cursor.execute(sqlStatement)
        connection.commit()
        resp = cursor.fetchall()

        # Elimina cada token de la consulta
        for i in resp:
            try:
                sqlStatement = 'DELETE FROM token WHERE Valor = "' + i[0] + '"'
                cursor.execute(sqlStatement)
                connection.commit()

            # Escribe en el log de eventos
                current_time = datetime.now()
                current_time_formated = current_time.strftime(format)
                file.write(current_time_formated + "; Eliminando token " +
                           i[0] + " de la base de datos \n")

            # Envía un mensaje para que se desencole otro usuario

                connectionQ = pika.BlockingConnection(
                    pika.ConnectionParameters(host='127.0.0.1'))
                channel = connectionQ.channel()
                channel.basic_publish(
                    exchange='', routing_key="desencolar", body=i[2])

            # Vuelve a escribir en el log de eventos
                current_time = datetime.now()
                current_time_formated = current_time.strftime(format)
                file.write(current_time_formated +
                           "; Enviando mensaje para desencolar;" + i[2] + "\n")
                file.flush()
            except (Exception, mariadb.Error) as error:
                if (connection):
                    print("Failed ", error)
            finally:
                # closing database connection.
                if (connection):
                    cursor.close()
                    connection.close()

    except (Exception, mariadb.Error) as error:
        print("Failed ", error)

    # Espera 10 segundos para volver a realizar la acción
    time.sleep(10)
