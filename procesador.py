from prueba import Proceso
from prueba import ListaProcesos
import time

#class procesador:
#    process= Proceso()
 
class Procesador:
    def __init__(self,lista):
        self.lista = lista

    def execLista(self):
        for proceso in self.lista:
            print('Nuevo proceso (ID: {}) leído.\nTiempo de arribo: {} segundos.\nAlmacenando...\n'.format(proceso.pID, proceso.tda))
            # time.sleep: Para la ejecución del código simulando una espera en segundos.
            time.sleep(int(proceso.tda))
            print('Proceso {} almacenado.\nSu prioridad es <<{}>>.\nTiempo necesario del procesador: {} segundos.\nEjecutando proceso...'.format(proceso.pID, proceso.pdp, proceso.tdp))
            time.sleep(int(proceso.tdp))
            print('Proceso finalizado.')
            print("--------------------------------------------------------------\n")

Procesos = ListaProcesos()
# Procesos.getProcesos()
Procesador = Procesador(Procesos)
Procesador.execLista()