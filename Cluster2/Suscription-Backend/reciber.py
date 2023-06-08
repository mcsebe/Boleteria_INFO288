import pika
import mariadb
import time
from datetime import datetime, timedelta
from common import *
import logging


###############################################################################
def get_connection_db(conn):
    return mariadb.connect(user=conn["user"],
                            password=conn["pass"],
                            host=conn["host"],
                            port=conn["port"],
                            database=conn["database"])

###############################################################################
time.sleep(60)
# Establecer la conexión con RabbitMQ
credentials = pika.PlainCredentials(sysConnConfig["rabbit"]["user"],sysConnConfig["rabbit"]["password"])
connection = pika.BlockingConnection(pika.ConnectionParameters("rabbitmq",5672,'/',credentials))
channel = connection.channel()


logging.getLogger("pika").propagate = False
logger = logging.getLogger()
logger.setLevel(logging.INFO)
handler = logging.FileHandler(sysConnConfig["log_rute"])
handler.setFormatter(logging.Formatter('%(asctime)s;%(message)s', datefmt="%H:%M:%S;%d/%m/%Y"))
logger.addHandler(handler)

counters = { }

# Declaración de las colas e inicio de contador
for i in sysConnConfig["Queues"].keys():
    channel.queue_declare(queue=i)
    counters[i] = 0

# Se encarga de escuchar las colas y desencolar
while True:
    for queue in sysConnConfig["Queues"].keys():
        # Si no se excede el límite, se añade el token a la base de datos
        if queue != "desencolar" and counters[queue] < sysConnConfig["Queues"][queue]:
            method, properties, body = channel.basic_get(queue=queue, auto_ack=True)
            if method:
                counters[queue] +=1
                # Añadiendo el token a la base de datos
                try:
                    # Obtener el timestamp actual
                    timestampNow = int(time.time())
                    # Sumar 5 minutos
                    timestampFuture = datetime.fromtimestamp(timestampNow) + timedelta(minutes=sysConnConfig["time_exp"])
                    # Convertir a timestamp Unix
                    timestampFuture = int(timestampFuture.timestamp())

                    connection = get_connection_db(sysConnConfig["dbConnConfig"])
                    cursor = connection.cursor()

                    sqlStatement = """INSERT INTO token (Valor, Fecha, Cola) VALUES (%s, %s, %s)"""

                    cursor.execute(sqlStatement, (body.decode(), timestampFuture, queue))
                    connection.commit()
                    
                    sqlStatement = """INSERT INTO all_tokens (Valor, Fecha, Cola) VALUES (%s, %s, %s)"""

                    cursor.execute(sqlStatement, (body.decode(), datetime.now(), queue))
                    connection.commit()

                    # Escribe en el log de eventos
                    logger.info("Añadiendo token " + body.decode() + " a la base de datos;" + str(timestampFuture) + ";" + queue)

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
            # Permite pasar otro
            method, properties, body = channel.basic_get(queue=queue, auto_ack=True)
            if method:
                counters[body.decode()] -= 1
                if(counters[body.decode()] < 0):
                    counters[body.decode()] = 0 

                # Escribe en el log de eventos
                logger.info("Dejar pasar otro token;" + body.decode())

            else:
                pass