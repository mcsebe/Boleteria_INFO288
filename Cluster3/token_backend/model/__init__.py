import mariadb

###############################################################################
def get_connection_db(conn):
    return mariadb.connect(user=conn["user"],
                            password=conn["pass"],
                            host=conn["host"],
                            port=conn["port"],
                            database=conn["database"])

###############################################################################


def token(dbConnConfig, token):
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
    print(resp)
    if len(resp) == 1:
        return "SI"
    else:
        return "NO"



