import mariadb

###############################################################################
def get_connection_db(conn):
    return mariadb.connect(user=conn["user"],
                            password=conn["pass"],
                            host=conn["host"],
                            port=conn["port"],
                            database=conn["database"])

###############################################################################


def token(dbConnConfig, data):
    resp=[]
    try:
        connection = get_connection_db(dbConnConfig)
        cursor = connection.cursor()
        sqlStatement = """SELECT * FROM token where valor = %s"""
        cursor.execute(sqlStatement, [token])
        resp = cursor.fetchall()
        resp = [item for sublist in resp for item in sublist]

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
    if resp != []:
        return True
    else:
        return False



