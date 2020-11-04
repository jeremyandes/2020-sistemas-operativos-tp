def CargaArchivo(): #Martin Carga de archivo, procesos almacenados en list procesos
    f = open ("procesos.txt", "r")

    procesos = list()

    for linea in f.readlines():
        proceso=linea.split('.') #Almacena el salto de linea (chequear)
        procesos.append(proceso)

    f.close()
