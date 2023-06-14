import mariadb
from datetime import datetime, timedelta
import os
import re

###############################################################################

def get_connection_db(conn):
    return mariadb.connect(user=conn["user"],
                           password=conn["pass"],
                           host=conn["host"],
                           port=conn["port"],
                           database=conn["database"])

###############################################################################

#Limpia los strings de "" ; \
def clean(unverified_input):
    return(re.sub(r'[\'";]', '', unverified_input))

# Función que realiza la consulta a la base de datos por un token en específico
def token(dbConnConfig, token, name, logger):
    resp = []
    # Realiza la consulta a la base de datos
    try:
        connection = get_connection_db(dbConnConfig)
        cursor = connection.cursor()
        sqlStatement = 'SELECT * FROM token WHERE Valor = %s'
        cursor.execute(sqlStatement,(clean(token),))
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

    # Si el token existe retorna "SI", en caso contrario retorna "NO"
    if len(resp) == 1:
        logger.info("Consulta sobre token " + token + ";SI;" + name)

        return "SI"
    else:
        logger.info("Consulta sobre token " + token + ";NO;" + name)
        return "NO"
