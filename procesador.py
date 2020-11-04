from cargaListas import CargaListas
from cargaTXT import CargaArchivo
from ordenaListas import OrdenaLlegada
from ordenaListas import OrdenaID
from ordenaListas import OrdenaPDP
from ordenaListas import OrdenaTDP
import time

#PRUEBA 1: supuse que pueden haber más archivos con procesos y pensé en modularizar y repetir procedimientos en cada lectura de archivo.
#Lo mismo que vamos a desarrollar para una sola lectura de archivo, lo dejo seteado en caso de que hayan más.

def iniciaProcesador():
    listasProcesos = CargaListas()
    for archivo in listasProcesos:
        print("\n{}".format(archivo))
        Procesos = CargaArchivo(archivo)
        print("--------------------------------------------------------------\n")
        for proceso in Procesos:
            print('Proceso (ID: {}) leído.\nTiempo de arribo: {} segundos.\nAlmacenando...\n'.format(proceso[0], proceso[1]))
            # time.sleep: Para la ejecución del código simulando una espera en segundos.
            time.sleep(int(proceso[1]))
            print('Proceso {} almacenado.\nSu prioridad es <<{}>>.\nTiempo necesario del procesador: {} segundos.\nEjecutando proceso...'.format(proceso[0], proceso[2], proceso[3]))
            time.sleep(int(proceso[3]))
            print('\n<<<<<Proceso finalizado.>>>>>')
            print("--------------------------------------------------------------\n")
        print("\n===============================================================\n")

        
        
        #prueba de ordenamientos de listas: FUNCIONANDO
        print("\nLista ordenada por 'ID' (campo 1):\n")

        listaNueva = OrdenaID(Procesos)
        for item in listaNueva:
            print(item)

        print("\nLista ordenada por 'Órden de Llegada' (campo 2):\n")

        listaNueva = OrdenaLlegada(Procesos)
        for item in listaNueva:
            print(item)        

        print("\nLista ordenada por 'PDP' (campo 3):\n")
        
        listaNueva = OrdenaPDP(Procesos)
        for item in listaNueva:
            print(item)

        print("\nLista ordenada por 'TDP' (campo 4):\n")

        listaNueva = OrdenaTDP(Procesos)
        for item in listaNueva:
            print(item)
        
        


iniciaProcesador()


