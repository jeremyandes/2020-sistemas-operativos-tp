import time
from Timer import minSec
from ordenaListas import OrdenaPor

#campo 0 = PID // campo 1 = tiempo de arribo // campo 2 = prioridad // campo 3 = tiempo de procesador
#campo 4 = tiempo de cpu // campo 5 = tiempo de respuesta // campo 6 = turnaround // campo 7 = tiempo de espera
def prioridadesDesalojo(Procesos):
    #utilizo una lista de procesos terminados con los datos de ejecución, respuesta, turnaround y espera
    terminados = list()
    #cola de procesos que se van a ejecutar
    colaEjecucion = list()
    #contador = tiempo de ejecución
    contador = 0
    #Utilizando este algoritmo, las ejecuciones son segundo a segundo. Mientras que alguna de las 2 listas tenga procesos o todavía tenga procesos
    while Procesos or colaEjecucion:
        #si hay procesos por arribar
        if Procesos:
            #me baso en el proceso 0
            proceso = Procesos[0]
            #si el tiempo de ejecución actual es igual al tiempo de arribo del proceso
            if contador == proceso[1]:
                #lo grabo en la cola de ejecución y lo borro de la lista de Procesos
                colaEjecucion.append(proceso)
                Procesos.pop(0)
        #si hay procesos en la cola de ejecución, se procesa en la función, retornando "colaEjecución", "terminados" y "contador", y en este caso, sólo pasó 1 segundo de tiempo de ejecución
        if colaEjecucion:
            colaEjecucion, terminados, contador = procesaCola(colaEjecucion,contador,terminados)
            time.sleep(1)
    #ejecución finalizada, retorno la lista de procesos con todos sus datos
    return terminados

def procesaCola(cola, contador, terminados):
    #ordeno por campo prioridad
    cola = OrdenaPor(2,cola)
    #me baso siempre en el primer proceso de la cola
    item = cola[0]
    #le resto un segundo de tiempo de procesador
    item[3] -= 1
    #si todavía no se ejecutó este proceso
    if item[4] == 0:
        #se le asigna el tiempo de respuesta
        item[5] = contador - item[1]
    #incremento un segundo de tiempo de ejecución
    item[4] += 1
    #iteración en la cola
    for proceso in cola:
        #incremento un segundo de espera a todos los procesos que NO sean el primer proceso, ya que se está ejecutando
        if proceso != cola[0]:
            proceso[7] += 1
    #incremento un segundo de timepo de ejecución
    contador += 1
    #si el proceso en ejecución finalizó
    if item[3]<=0:
        print("[{}]     Proceso ID={} finalizado.".format(minSec(contador),item[0]))
        #se le asugna el turnaround
        item[6] = contador - item[1]
        #se guarda en la lista de terminados
        terminados.append(item)
        #se borra de la cola de ejecución
        cola.pop(0)
    #retorna la cola de ejecución, la lista de terminados y el tiempo de ejecución.
    return (cola, terminados, contador)

# La ejecución del archivo que tenemos es así (borren los print que los hice probando nomás):
# Entra 9988 al segundo 0 con p 2 y se ejecuta
# Entra 1928 al segundo 5 con p 1 y se ejecuta, 9988 queda en t 4
# Entra 1200 al segundo 7 con p 10
# Entra 7794 al segundo 8 con p 15
# Entra 2500 al segundo 10 con p 12
# Finaliza 1928, se ejecuta 9988 al segundo 11
# Finaliza 9988, se ejecuta 1200 al segundo 15
# Finaliza 1200, se ejecuta 2500 al segundo 21
# Finaliza 2500, se ejecuta 7794 al seugundo 26
# Finaliza todo al segundo 34