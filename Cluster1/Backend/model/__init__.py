import mariadb
import pika
from datetime import datetime
import os

###############################################################################


def get_connection_db(conn):
    print(conn)
    return mariadb.connect(user=conn["user"],
                           password=conn["pass"],
                           host=conn["host"],
                           port=conn["port"],
                           database=conn["database"])

###############################################################################


# Función que retorna los asientos ya reservados de un concierto

def available(dbConnConfig, concert):
    resp = []
    connection = 0
    try:

        connection = get_connection_db(dbConnConfig)
        cursor = connection.cursor()
        sqlStatement = """SELECT t.Asiento, COALESCE(count(r.Asiento), 0) AS Suma_Asientos FROM ( SELECT 'Galeria' AS Asiento UNION ALL SELECT 'Cancha' AS Asiento UNION ALL SELECT 'Andes' AS Asiento ) AS t LEFT JOIN reserva AS r ON r.Asiento = t.Asiento AND r.id_concierto = (%s) GROUP BY t.Asiento"""
        cursor.execute(sqlStatement, [concert])
        resp = cursor.fetchall()
        resp = [item for sublist in resp for item in sublist]

    except (Exception, mariadb.Error) as error:
        resp = str(error)
        if (connection):
            print("Failed select ", error)

    finally:
        if (connection):
            cursor.close()
            connection.close()

    return resp

# Función que retorna la información general de un concierto que se encuentra en la base de datos


def information(dbConnConfig, concert):
    resp = []
    connection = 0
    try:
        connection = get_connection_db(dbConnConfig)
        cursor = connection.cursor()

        sqlStatement = """SELECT * FROM concierto WHERE id = (%s)"""
        cursor.execute(sqlStatement, [concert])
        resp = cursor.fetchall()
        resp = [item for sublist in resp for item in sublist]

    except (Exception, mariadb.Error) as error:
        resp = str(error)
        if (connection):
            print("Failed select ", error)

    finally:
        if (connection):
            cursor.close()
            connection.close()

    return resp

# Función que retorna la localización en la que se realizará un concierto


def location(dbConnConfig, concert):
    resp = []
    connection = 0
    try:
        connection = get_connection_db(dbConnConfig)
        cursor = connection.cursor()

        sqlStatement = """SELECT * FROM locacion JOIN concierto ON locacion.id = concierto.id_locacion WHERE concierto.id = (%s)"""
        cursor.execute(sqlStatement, [concert])
        resp = cursor.fetchall()
        resp = [item for sublist in resp for item in sublist]

    except (Exception, mariadb.Error) as error:
        resp = str(error)
        if (connection):
            print("Failed select ", error)

    finally:
        if (connection):
            cursor.close()
            connection.close()

    return resp

# Función que inserta en la base de datos la información de la reserva, elimina el token correspondiente y envía un mensaje a la cola

def insert(dbConnConfig, dbConnConfig2, data, logger, Rabbit):
    connection = 0
    # Elimina el token que correspondiente al usuario
    try:
        connection = get_connection_db(dbConnConfig2)
        cursor = connection.cursor()

        sqlStatement = 'DELETE FROM token WHERE Valor = "' + \
            data["Token"] + '"'
        print(sqlStatement)

        cursor.execute(sqlStatement)
        connection.commit()

        logger.info("Eliminando token " + data["Token"] + " de la base de datos")

    except (Exception, mariadb.Error) as error:
        if (connection):
            print("Failed delete one ", error)

    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()

    resp = {"inserted_rows": -1}
    
    # Se inserta la información del formulario en la base de datos
    try:
        connection = get_connection_db(dbConnConfig)
        cursor = connection.cursor()

        sqlStatement = """INSERT INTO reserva (Asiento, Nombre, Rut, Edad, Correo, id_concierto, TiempoSelec, TiempoPago, Precio) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""

        cursor.execute(sqlStatement, (data["Asiento"], data["Nombre"], data["Rut"], int(data["Edad"]), data["Correo"], int(data["Id_concierto"]), data["T1"], data["T2"], int(data["Price"])))
        connection.commit()
        resp["inserted_rows"] = cursor.rowcount

        logger.info("Insertando en la tabla reserva " + str(data["Asiento"]) + ";" + data["Nombre"] + ";" + data["Rut"] + ";" + str(data["Edad"]) + ";" + data["Correo"] + ";" + str(data["Id_concierto"]))

    except (Exception, mariadb.Error) as error:
        resp = str(error)
        if (connection):
            print("Failed insert one ", error)

    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()

    # Se envía un mensaje para que se desencole un nuevo usuario
    credentials = pika.PlainCredentials(Rabbit["user"],Rabbit["password"])
    connection = pika.BlockingConnection(pika.ConnectionParameters("rabbitmq",5672,'/',credentials))
    channel = connection.channel()
    channel.basic_publish(
        exchange='', routing_key="desencolar", body=data["Nombre_Concierto"])

    logger.info("Enviando mensaje para desencolar;" + data["Nombre_Concierto"])

    return resp
