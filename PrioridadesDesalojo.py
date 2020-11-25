import time
from Timer import minSec
from ordenaListas import OrdenaPor

#campo 0 = PID // campo 1 = tiempo de arribo // campo 2 = prioridad // campo 3 = tiempo de procesador
#campo 4 = tiempo de cpu // campo 5 = tiempo de respuesta // campo 6 = turnaround // campo 7 = tiempo de espera
def prioridadesDesalojo(Procesos):
    Procesos = OrdenaPor(1,Procesos)
    terminados = list()
    colaEjecucion = list()
    contador = 0
    print("----------------------------------------------------\n")
    while Procesos or colaEjecucion:
        if Procesos:
            proceso = Procesos[0]
            if contador == proceso[1]:
                colaEjecucion.append(proceso)
                print("[{}]     Proceso ID={} cargado.".format(minSec(contador),proceso[0]))
                Procesos.pop(0)
        if colaEjecucion:
            colaEjecucion, terminados, contador = procesaCola(colaEjecucion,contador,terminados)
            #time.sleep(1)
    print("EJECUCIÓN FINALIZADA")
    return terminados

def procesaCola(cola, contador, terminados):
    cola = OrdenaPor(2,cola)
    item = cola[0]
    item[3] -= 1
    if item[4] == 0:
        item[5] = contador - item[1]
    item[4] += 1
    for proceso in cola:
        if proceso != cola[0]:
            proceso[7] += 1
    contador += 1
    if item[3]<=0:
        print("[{}]     Proceso ID={} finalizado.".format(minSec(contador),item[0]))
        item[6] = contador - item[1]
        terminados.append(item)
        cola.pop(0)
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