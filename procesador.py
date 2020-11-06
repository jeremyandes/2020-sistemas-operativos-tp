from CargaTxt import CargaArchivo
# from ordenaListas import OrdenaLlegada
# from ordenaListas import OrdenaID
# from ordenaListas import OrdenaPDP
# from ordenaListas import OrdenaTDP
from ordenaListas import OrdenaPor
import time



def iniciaProcesador(archivo):
    
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
    print("\nLista ordenada por 'ID' (campo 0):\n")

    # listaNueva = OrdenaID(Procesos)
    listaNueva = OrdenaPor(0,Procesos)
    for item in listaNueva:
        print(item)

    print("\nLista ordenada por 'Órden de Llegada' (campo 1):\n")

    # listaNueva = OrdenaLlegada(Procesos)
    listaNueva = OrdenaPor(1,Procesos)
    for item in listaNueva:
        print(item)        

    print("\nLista ordenada por 'PDP' (campo 2):\n")
        
    # listaNueva = OrdenaPDP(Procesos)
    listaNueva = OrdenaPor(2,Procesos)
    for item in listaNueva:
        print(item)

    print("\nLista ordenada por 'TDP' (campo 3):\n")

    # listaNueva = OrdenaTDP(Procesos)
    listaNueva = OrdenaPor(3,Procesos)
    for item in listaNueva:
        print(item)

iniciaProcesador("lista1.txt")
        





