import time
from Timer import iniciaTimer
from Timer import minSec
from ordenaListas import OrdenaPor

#campo 0 = PID // campo 1 = tiempo de arribo // campo 2 = prioridad // campo 3 = tiempo de procesador
#campo 4 = tiempo de respuesta // campo 5 = turnaround // campo 6 = tiempo de cpu // campo 7 = tiempo de espera
def prioridadesSinDesalojo(Procesos):
    terminados = list()
    colaEjecucion = list()
    contador = 0
    while Procesos or colaEjecucion:
        nuevos = list ()
        if Procesos:
            for proceso in Procesos:
                if contador >= proceso[1]:
                    colaEjecucion.append(proceso)
                    nuevos.append(proceso)
                if not nuevos and Procesos:
                    contador += 1
                    time.sleep(1)
        if colaEjecucion:
            colaEjecucion, terminados, contador = procesaCola(colaEjecucion,contador,terminados)
        if nuevos:
            for nuevo in nuevos:
                Procesos.remove(nuevo)
    return terminados

def procesaCola(cola, contador, terminados):
    cola = OrdenaPor(2,cola)
    item = cola[0]
    time.sleep(item[3])
    item[4] = item[3]
    item[5] = contador - item[1]
    contador += item[3]
    print("[{}]     Proceso ID={} finalizado.\n".format(minSec(contador),item[0]))
    item[6] = contador - item[1]
    item[7] = item[6] - item[4]
    terminados.append(item)
    cola.pop(0)
    return (cola, terminados, contador)

# La ejecución del archivo que tenemos es así (borren los print que los hice probando nomás):
# Se ejecuta 9988 al segundo 0 y finaliza al 9.
# Se ejecuta 1928 al segundo 9 y finaliza al 16.
# Se ejecuta 1200 al segundo 16 y finaliza al 22.
# Se ejecuta 2500 al segundo 22 y finaliza al 27.
# Se ejecuta 7794 al segundo 27 y finaliza al 35