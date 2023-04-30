from csv import reader
import os

# Función que lee el archivo .csv correspondiente y retorna los productos que se encuentran en el argumento
def select_productos(archivo, productos):
    # Obtiene la ruta actual
    d = os.getcwd()

    #Ruta en windows
    archivoW = d + "\\files\\"+ archivo
    retornar = []
    try:
        with open(archivoW, 'r') as csv_file:
            csv_reader = reader(csv_file)
            for i in list(csv_reader):
                    if(i[1] in productos):
                        retornar.append(i)
            return retornar
    
    #Ruta en linux
    except:
        archivoL = d + "/files/"+ archivo
        with open(archivoL, 'r') as csv_file:
            csv_reader = reader(csv_file)
            for i in list(csv_reader):
                    if(i[1] in productos):
                        retornar.append(i)
            return retornar

# Función que lee el archivo .csv correspondiente y retorna todos los productos de la categoría
def select_categoria(archivo):
    # Obtiene la ruta actual
    d = os.getcwd()

    #Ruta en windows
    archivoW = d + "\\files\\"+ archivo
    try:
        with open(archivoW, 'r') as csv_file:
            csv_reader = reader(csv_file)
            return list(csv_reader)
    #Ruta en linux
    except:
        archivoL = d + "/files/"+ archivo
        with open(archivoL, 'r') as csv_file:
            csv_reader = reader(csv_file)
            return list(csv_reader)
