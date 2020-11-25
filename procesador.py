from CargaTxt import CargaArchivo
# from ordenaListas import OrdenaLlegada
# from ordenaListas import OrdenaID
# from ordenaListas import OrdenaPDP
# from ordenaListas import OrdenaTDP
from ordenaListas import OrdenaPor
from Timer import iniciaTimer
import time



def iniciaProcesador(Procesos):
    print("--------------------------------------------------------------\n")
    for proceso in Procesos:
        print('Proceso (ID: {}) leído.\nTiempo de arribo: {} segundos.\n'.format(proceso[0], proceso[1]))
        #llamo a la funcion "iniciaTimer"
        iniciaTimer("Almacenando...", proceso[1])
        print('Proceso {} almacenado.\nSu prioridad es <<{}>>.\nTiempo necesario del procesador: {} segundos.\n'.format(proceso[0], proceso[2], proceso[3]))
        #llamo a la funcion "iniciaTimer"
        iniciaTimer("Ejecutando proceso...", proceso[3])
        print('\n<<<<<Proceso finalizado.>>>>>')
        print("--------------------------------------------------------------\n")
    print("\n===============================================================\n")

def muest_lista(listaNueva):
    for item in listaNueva:
        print(item) 


#prueba de ordenamientos de listas: FUNCIONANDO
""" print("\nLista ordenada por 'ID' (campo 0):\n")
# listaNueva = OrdenaID(Procesos)
    listaNueva = OrdenaPor(0,Procesos)
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
        print(item) """


