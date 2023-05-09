import mariadb
import pika
from datetime import datetime
import os

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

    return resp

def informacion(dbConnConfig, concierto):
    resp=[]
    try:
        connection = get_connection_db(dbConnConfig)
        cursor = connection.cursor()

        sqlStatement = """SELECT * FROM concierto WHERE id = (%s)"""
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

    return resp

def localizacion(dbConnConfig, concierto):
    resp=[]
    try:
        connection = get_connection_db(dbConnConfig)
        cursor = connection.cursor()

        sqlStatement = """SELECT * FROM locacion JOIN concierto ON locacion.id = concierto.id_locacion WHERE concierto.id = (%s)"""
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

    return resp


def insert(dbConnConfig, dbConnConfig2, data):

    formato = "%H:%M:%S;%d/%m/%Y"
    #Ruta en windows
    archivoW = os.getcwd() + "\\Log\\"+ "logs.txt"
    try:
        file = open(archivoW, 'a+')
    #Ruta en linux
    except:
        archivoL = os.getcwd() + "/files/"+ "logs.txt"
        file = open(archivoL, 'a+')

    try:
        connection = get_connection_db(dbConnConfig2)
        cursor = connection.cursor()

        sqlStatement = 'DELETE FROM token WHERE Valor = "' + data["Token"] + '"'
        print(sqlStatement)

        cursor.execute(sqlStatement)
        connection.commit()

        fecha_hora_actual = datetime.now()
        fecha_hora_formateada = fecha_hora_actual.strftime(formato)
        file.write(fecha_hora_formateada + "; Eliminando token " +  data["Token"] + " de la base de datos \n")

    except (Exception, mariadb.Error) as error :
        if(connection):
            print("Failed delete one ", error)

    finally:
        #closing database connection.
        if(connection):
            cursor.close()
            connection.close()

    resp={"inserted_rows":-1}
    try:
        connection = get_connection_db(dbConnConfig)
        cursor = connection.cursor()

        sqlStatement = """INSERT INTO reserva (Asiento, Nombre, Rut, Edad, Correo, id_concierto) VALUES (%s, %s, %s, %s, %s, %s)"""

        cursor.execute(sqlStatement, (int(data["Asiento"]), data["Nombre"], data["Rut"], int(data["Edad"]), data["Correo"], int(data["Id_concierto"])))
        connection.commit()
        resp["inserted_rows"] = cursor.rowcount

        fecha_hora_actual = datetime.now()
        fecha_hora_formateada = fecha_hora_actual.strftime(formato)
        file.write(fecha_hora_formateada + "; Insertando en la tabla reserva "  + str(data["Asiento"]) + ";" + data["Nombre"] + ";" + data["Rut"] + ";"  + str(data["Edad"]) + ";" + data["Correo"] + ";" + str(data["Id_concierto"]) + "\n")


    except (Exception, mariadb.Error) as error :
        resp=str(error)
        if(connection):
            print("Failed insert one ", error)

    finally:
        #closing database connection.
        if(connection):
            cursor.close()
            connection.close()

    connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1'))
    channel = connection.channel()
    channel.basic_publish(exchange='', routing_key="desencolar", body = data["Nombre_Concierto"])

    fecha_hora_actual = datetime.now()
    fecha_hora_formateada = fecha_hora_actual.strftime(formato)
    file.write(fecha_hora_formateada + "; Enviando mensaje para desencolar;" + data["Nombre_Concierto"] +"\n")

    file.close()

    return resp


    # # ----------------------------------------------------------------------------
    # fecha_hora_actual = datetime.now()
    # fecha_hora_formateada = fecha_hora_actual.strftime(formato)

    # file.write(fecha_hora_formateada + "; Encolando token " + mensaje + ";" + ruta + "\n")
    # file.close()
    # # ----------------------------------------------------------------------------