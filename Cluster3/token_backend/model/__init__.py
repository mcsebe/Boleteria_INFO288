import mariadb
from datetime import datetime, timedelta
import os

###############################################################################

def get_connection_db(conn):
    return mariadb.connect(user=conn["user"],
                           password=conn["pass"],
                           host=conn["host"],
                           port=conn["port"],
                           database=conn["database"])

###############################################################################


# Función que realiza la consulta a la base de datos por un token en específico
def token(dbConnConfig, token, name, format):
    resp = []
    # Realiza la consulta a la base de datos
    try:
        connection = get_connection_db(dbConnConfig)
        cursor = connection.cursor()
        sqlStatement = 'SELECT * FROM token WHERE Valor ="' + token + '"'
        cursor.execute(sqlStatement)
        resp = cursor.fetchall()

    except (Exception, mariadb.Error) as error:
        resp = []
        if (connection):
            print("Failed select ", error)

    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()
            print("MariaDB connection is closed")

    # Escribe en el log de eventos
    current_time = datetime.now()
    current_time_formated = current_time.strftime(format)

    # Si el token existe retorna "SI", en caso contrario retorna "NO"
    if len(resp) == 1:
        logW = os.getcwd() + "\\Log\\" + "logs.txt"
        try:
            file = open(logW, 'a+')
        except:
            logL = os.getcwd() + "/files/" + "logs.txt"
            file = open(logL, 'a+')
        file.write(current_time_formated + "; Consulta sobre token " + token + ";SI;" + name + "\n")

        return "SI"
    else:
        logW = os.getcwd() + "\\Log\\" + "logs.txt"
        try:
            file = open(logW, 'a+')
        except:
            logL = os.getcwd() + "/files/" + "logs.txt"
            file = open(logL, 'a+')
        file.write(current_time_formated + "; Consulta sobre token " + token + ";NO;" + name + "\n")

        return "NO"
