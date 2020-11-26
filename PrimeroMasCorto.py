import time
from Timer import iniciaTimer
from Timer import minSec
from ordenaListas import OrdenaPor

#campo 0 = PID // campo 1 = tiempo de arribo // campo 2 = prioridad // campo 3 = tiempo de procesador
#campo 4 = tiempo de cpu // campo 5 = tiempo de respuesta // campo 6 = turnaround // campo 7 = tiempo de espera
def primeroMasCorto(Procesos):
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
                if not nuevos:
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
    #ordeno por campo "tiempo de ejecución"
    cola = OrdenaPor(3,cola)
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

# La ejecución correcta sería así:

# Proceso ID=9988 CARGADO al segundo 0 <<< tiempo de ejecución 8 segundos
# Proceso ID=1928 CARGADO al segundo 5 <<<
# Proceso ID=1200 CARGADO al segundo 7 <<<
# Proceso ID=7794 CARGADO al segundo 8 <<<
#                                         Proceso ID=9988 finalizado al segundo 8.
# Proceso ID=2500 CARGADO al segundo 10 <<<
#                                         Proceso ID=1200 finalizado al segundo 14.
#                                         Proceso ID=2500 finalizado al segundo 19.
#                                         Proceso ID=1928 finalizado al segundo 26.
#                                         Proceso ID=7794 finalizado al segundo 34.