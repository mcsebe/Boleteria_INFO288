import mariadb
import pika

###############################################################################
def get_connection_db(conn):
    return mariadb.connect(user=conn["user"],
                            password=conn["pass"],
                            host=conn["host"],
                            port=conn["port"],
                            database=conn["database"])

###############################################################################

def capacidad(dbConnConfig, concierto):
    resp=[]
    try:
        connection = get_connection_db(dbConnConfig)
        cursor = connection.cursor()
        sqlStatement = """SELECT locacion.capacidad FROM locacion JOIN concierto ON locacion.id = concierto.id_locacion WHERE concierto.id = (%s)"""
        cursor.execute(sqlStatement, [concierto])
        resp = cursor.fetchall()
        resp = [item for sublist in resp for item in sublist]

    except (Exception, mariadb.Error) as error :
        resp=str(error)
        if(connection):
            print("Failed select ", error)

    finally:
        #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("MariaDB connection is closed")

    return resp

def disponible(dbConnConfig, concierto):
    resp=[]
    try:
        connection = get_connection_db(dbConnConfig)
        cursor = connection.cursor()

        sqlStatement = """SELECT asiento FROM reserva WHERE id_concierto = (%s)"""
        cursor.execute(sqlStatement, [concierto])
        resp = cursor.fetchall()
        resp = [item for sublist in resp for item in sublist]

    except (Exception, mariadb.Error) as error :
        resp=str(error)
        if(connection):
            print("Failed select ", error)

    finally:
        #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

    return resp


def insert(dbConnConfig, data):
    resp={"inserted_rows":-1}
    try:
        connection = get_connection_db(dbConnConfig)
        cursor = connection.cursor()

        sqlStatement = """INSERT INTO reserva (Asiento, Nombre, Rut, Edad, Correo, id_concierto) VALUES (%s, %s, %s, %s, %s, %s)"""

        cursor.execute(sqlStatement, (int(data["Asiento"]), data["Nombre"], data["Rut"], int(data["Edad"]), data["Correo"], int(data["id_concierto"])))
        connection.commit()
        resp["inserted_rows"] = cursor.rowcount

    except (Exception, mariadb.Error) as error :
        resp=str(error)
        if(connection):
            print("Failed insert one ", error)

    finally:
        #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1'))
    channel = connection.channel()
    channel.basic_publish(exchange='', routing_key="desencolar", body = data["NombreConcierto"])
    return resp