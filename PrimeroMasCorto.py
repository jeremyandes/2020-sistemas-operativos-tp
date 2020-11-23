import time
from Timer import iniciaTimer
from ordenaListas import OrdenaPor

def primeroMasCorto(Procesos):
    Procesos = OrdenaPor(1,Procesos)
    colaEjecucion = list()
    contador = 0
    print("----------------------------------------------------\n")
    while Procesos or colaEjecucion:
        if Procesos:
            proceso = Procesos[0]
            if contador == proceso[1]:
                colaEjecucion.append(proceso)
                print("Proceso ID={} CARGADO al segundo {} <<<".format(proceso[0],contador))
                Procesos.pop(0)

        colaEjecucion = procesaCola(colaEjecucion,contador)
        contador += 1
        time.sleep(1)
    print("EJECUCIÓN FINALIZADA")     

def procesaCola(cola, contador):
    #cola ordenada por campo 3 (tiempo de proceso)
    cola = OrdenaPor(3,cola)
    item = cola[0]
    item[3] -= 1
    if item[3]<=0:
        print("Proceso ID={} finalizado al segundo {}.".format(item[0],contador))
        cola.pop(0)
    return cola

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