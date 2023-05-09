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
formato = "%H:%M:%S;%d/%m/%Y"

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


        # ----------------------------------------------------------------------------
        #Ruta en windows
        archivoW = os.getcwd() + "\\Log\\"+ "logs.txt"
        try:
            file =  open(archivoW, 'a+')
        #Ruta en linux
        except:
            archivoL = os.getcwd() + "/files/"+ "logs.txt"
            file = open(archivoL, 'a+')
        # ----------------------------------------------------------------------------

        for i in resp:
            try:
                sqlStatement = 'DELETE FROM token WHERE Valor = "' + i[0] + '"'
                cursor.execute(sqlStatement)
                connection.commit()

            # ----------------------------------------------------------------------------
                fecha_hora_actual = datetime.now()
                fecha_hora_formateada = fecha_hora_actual.strftime(formato)
                file.write(fecha_hora_formateada + "; Eliminando token " + i[0] + " de la base de datos \n")
            # ----------------------------------------------------------------------------    

                connectionQ = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1'))
                channel = connectionQ.channel()
                channel.basic_publish(exchange='', routing_key="desencolar", body = i[2])
                
            # ----------------------------------------------------------------------------
                fecha_hora_actual = datetime.now()
                fecha_hora_formateada = fecha_hora_actual.strftime(formato)
                file.write(fecha_hora_formateada + "; Enviando mensaje para desencolar;" + i[2] +"\n")
            # ----------------------------------------------------------------------------  


            except (Exception, mariadb.Error) as error :
                if(connection):
                    print("Failed ", error)

        file.close()

    except (Exception, mariadb.Error) as error :
        if(connection):
            print("Failed ", error)

    finally:
        #closing database connection.
        if(connection):
            cursor.close()
            connection.close()

    time.sleep(10)