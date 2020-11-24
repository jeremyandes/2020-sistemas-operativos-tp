#sublibrería "path" de la librería "os"
import os.path
#librería "sys" del sistema
import sys

def CargaArchivo(nombArch): #Paso por parámetro el nombre del archivo, ingresado desde la linea de comando

    #abro el archivo especificado, utilizando el parámetro "nombArch"
    try:
        f=open(nombArch,'r')
    except OSError:
        sys.exit("El archivo '{}' no existe".format(nombArch))
    else:
        #os.path.getsize >> Retorna el peso del archivo
        filesize = os.path.getsize(nombArch)

        #si el archivo tiene contenido
        if filesize != 0:
            #inicializo la lista "procesos"
            procesos = list()

            #recorro el archivo
            for linea in f:
                #primero elimino el salto de línea "\n"
                proceso = linea.strip()
                #luego realizo un split retornando la lista correspondiente
                proceso = proceso.split('.')
                #guardo SOLAMENTE enteros
                for i in range(4):
                    proceso[i] = int(proceso[i])

                #validacion
                if proceso[0]>=1 and proceso[0]<=9999 and proceso[1]>=0 and proceso[1]<=99999 and proceso[2]>=1 and proceso[2]<=15 and proceso[3]>=0 and proceso[3]<=9999:
                    #agrego los campos faltantes para calcular los tiempos de cada proceso
                    for i in range(4):
                        proceso.append(0)

                    #grabo en la lista "procesos" el "proceso" resultante
                    procesos.append(proceso)

                    #verifico que se guardó
                    encontro = False
                    for busca in procesos:
                        if busca[0] == proceso[0]:
                            print("Proceso ID={} cargado correctamente.".format(int(proceso[0])))
                            encontro = True
                            break

                    #si terminó el recorrido y no lo encontró
                    if encontro is False:
                        #sys.exit = "Mata" la ejecución del código y cierra el programa
                        sys.exit("<<< ERROR: Proceso de ID={} no fue cargado correctamente. >>>".format(proceso[0]).center(20))

                else:
                    #sys.exit = "Mata" la ejecución del código y cierra el programa
                    sys.exit("<<< ERROR: Campos del proceso ID={}/TDA={}/PDP={}/TDP={} incorrectos. >>>".format(proceso[0],proceso[1]
                    ,proceso[2],proceso[3]).center(20))

            #cierro el archivo
            f.close()

            #retorno la lista de "procesos"
            return procesos
            
        else:
            sys.exit("<< ERROR: El archivo está vacío. >>".center(20))