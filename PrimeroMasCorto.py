import time
from Timer import iniciaTimer
from Timer import minSec
from ordenaListas import OrdenaPor

#campo 0 = PID // campo 1 = tiempo de arribo // campo 2 = prioridad // campo 3 = tiempo de procesador
#campo 4 = tiempo de respuesta // campo 5 = turnaround // campo 6 = tiempo de cpu // campo 7 = tiempo de espera
def primeroMasCorto(Procesos):
    Procesos = OrdenaPor(1,Procesos)
    terminados = list()
    colaEjecucion = list()
    contador = 0
    print("----------------------------------------------------\n")
    while Procesos or colaEjecucion:
        nuevos = list ()
        if Procesos:
            for proceso in Procesos:
                if contador >= proceso[1]:
                    colaEjecucion.append(proceso)
                    nuevos.append(proceso)
                    print("[{}]     Proceso ID={} cargado.".format(minSec(contador),proceso[0]))
                if not nuevos:
                    contador += 1
                    time.sleep(1)
        if colaEjecucion:
            colaEjecucion, terminados, contador = procesaCola(colaEjecucion,contador,terminados)
        if nuevos:
            for nuevo in nuevos:
                Procesos.remove(nuevo)
    print("EJECUCIÓN FINALIZADA")
    return terminados

def procesaCola(cola, contador, terminados):
    cola = OrdenaPor(3,cola)
    item = cola[0]
    print("\n")
    iniciaTimer(("Ejecutando Proceso ID={}".format(item[0])),item[3])
    item[4] = item[3]
    item[5] = contador - item[1]
    contador += item[3]
    print("[{}]     Proceso ID={} finalizado.".format(minSec(contador),item[0]))
    item[6] = contador - item[1]
    for proceso in cola:
        if proceso != cola[0]:
            proceso[7] += item[3]
    terminados.append(item)
    cola.pop(0)
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