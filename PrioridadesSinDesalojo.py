import time
from Timer import iniciaTimer
from Timer import minSec
from ordenaListas import OrdenaPor

#campo 0 = PID // campo 1 = tiempo de arribo // campo 2 = prioridad // campo 3 = tiempo de procesador
#campo 4 = tiempo de cpu // campo 5 = tiempo de respuesta // campo 6 = turnaround // campo 7 = tiempo de espera
def prioridadesSinDesalojo(Procesos):
    #utilizo una lista de procesos terminados con los datos de ejecución, respuesta, turnaround y espera
    terminados = list()
    #cola de procesos que se van a ejecutar
    colaEjecucion = list()
    #contador = tiempo de ejecución
    contador = 0
    #mientras que alguna de las 2 listas tenga procesos o todavía tenga procesos
    while Procesos or colaEjecucion:
        #lista auxiliar que cada vez que entre al ciclo va a estar vacía, la cual va a borrar todos los procesos que ésta contenga, de la lista de "Procesos"
        nuevos = list ()
        #si hay procesos por arribar
        if Procesos:
            for proceso in Procesos:
                #si el tiempo de ejecución actual es mayor o igual al tiempo de arribo del proceso actual del recorrido
                if contador >= proceso[1]:
                    #el proceso va a la cola y lo guardo en nuevos
                    colaEjecucion.append(proceso)
                    nuevos.append(proceso)
                #si no hay procesos nuevos pero todavía hay procesos por arribar, incremento un segundo de tiempo de espera al contador
                if not nuevos and Procesos:
                    contador += 1
                    time.sleep(1)
        #si hay procesos en la cola de ejecución, se procesa en la función, retornando "colaEjecución", "terminados" y "contador"
        if colaEjecucion:
            colaEjecucion, terminados, contador = procesaCola(colaEjecucion,contador,terminados)
        #si hubo procesos nuevos, los borro de la lista de "Procesos"
        if nuevos:
            for nuevo in nuevos:
                Procesos.remove(nuevo)
    #ejecución finalizada, retorno la lista de procesos con todos sus datos
    return terminados

def procesaCola(cola, contador, terminados):
    #ordeno por campo prioridad
    cola = OrdenaPor(2,cola)
    #me baso siempre en el primer proceso de la cola
    item = cola[0]
    #se ejecuta el proceso
    time.sleep(item[3])
    #se le asigna el tiempo de CPU
    item[4] = item[3]
    #se le asigna el tiempo de respuesta
    item[5] = contador - item[1]
    #se actualiza el contador al tiempo de ejecución actual
    contador += item[3]
    print("[{}]     Proceso ID={} finalizado.\n".format(minSec(contador),item[0]))
    #se le asigna el turnaround
    item[6] = contador - item[1]
    #se le asigna el tiempo de espera
    item[7] = item[6] - item[4]
    #se guarda en la lista de terminados
    terminados.append(item)
    #se borra de la cola de ejecución
    cola.pop(0)
    #retorna la cola de ejecución, la lista de terminados y el tiempo de ejecución
    return (cola, terminados, contador)

# La ejecución del archivo que tenemos es así:
# Se ejecuta 9988 al segundo 0 y finaliza al 9.
# Se ejecuta 1928 al segundo 9 y finaliza al 16.
# Se ejecuta 1200 al segundo 16 y finaliza al 22.
# Se ejecuta 2500 al segundo 22 y finaliza al 27.
# Se ejecuta 7794 al segundo 27 y finaliza al 35