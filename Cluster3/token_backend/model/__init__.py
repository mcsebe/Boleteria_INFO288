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


def token(dbConnConfig, token, name):
    resp=[]
    try:
        connection = get_connection_db(dbConnConfig)
        cursor = connection.cursor()
        sqlStatement = 'SELECT * FROM token WHERE Valor ="' + token + '"'
        cursor.execute(sqlStatement)
        resp = cursor.fetchall()

    except (Exception, mariadb.Error) as error :
        resp=[]
        if(connection):
            print("Failed select ", error)

    finally:
        #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("MariaDB connection is closed")

    # ----------------------------------------------------------------------------
    fecha_hora_actual = datetime.now()
    formato = "%H:%M:%S;%d/%m/%Y"
    fecha_hora_formateada = fecha_hora_actual.strftime(formato)

    #Ruta en windows
    archivoW = os.getcwd() + "\\Log\\"+ "logs.txt"
    try:
        file = open(archivoW, 'a+')
    #Ruta en linux
    except:
        archivoL = os.getcwd() + "/files/"+ "logs.txt"
        file = open(archivoL, 'a+')
    # ----------------------------------------------------------------------------

    if len(resp) == 1:

        file.write(fecha_hora_formateada + "; Consulta sobre token " + token + ";SI;" + name + "\n")
        file.close()

        return "SI"
    else:

        file.write(fecha_hora_formateada + "; Consulta sobre token " + token + ";NO;" + name +"\n")
        file.close()

        return "NO"



