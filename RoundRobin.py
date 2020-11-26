#Ejecucion de los procesos segun algoritmo de planificion: Round Robin, es de tipo apropiativa
import time
from termcolor import colored
from Timer import minSec

'''[0]ID [1]TArribo [2]prioridad [3]tiempo de procesador [4]tiempo de CPU
[5]tiempo de rta [6]turnaround [7]espera total'''

def round_robin(Procesos, quantum):
    inicio=time.time()                                                                  #Guardo el tiempo en el que se empezo a ejecutar el algoritmo
    terminados=[]                                                                       #defino la lista de procesos terminados como vacia
    while Procesos :                                                                    #Mientras la lista de procesos no este vacia
        borrados=[]                                                                     #inicializo la lista de borrados como vacía en el ciclo actual
        for act in Procesos:                                                            #Recorro cada proceso en la lista
            if act[1] <= (time.time()-inicio) :                                         #Si el tiempo de arribo es <= al tiempo transcurrido desde que comenzo el algoritmo
                if act[4] == 0 :                                                        #El proceso llego pero no se ejecuto tdv
                    act[5]= time.time() -inicio -act[1]                                 #guardo el seg en que se comenzo a ejecutarse el primer quantum desde su arribo
                if quantum > act[3] :                                                   #Si el tiempo restante del proceso es menor al quantum
                    time.sleep(act[3])
                    act[4]+=act[3]                                                      #se suma el tiempo en procesador
                else:
                    time.sleep(quantum)
                    act[4]+=quantum                                                     #se suma el tiempo en procesador
                act[3]-=quantum                                                         #Se resta el valor del quantum ya sea que se halla ejecutado completo o no
                if act[3]<=0 :                                                          #El proceso termino si su tiempo restante es menor o igual a cero
                    print("[{}]     Proceso ID={} finalizado.\n".format(minSec(int((time.time()-inicio))), act[0]))
                    act[6]= time.time() - inicio - act[1]                               #Guardo el tiempo TURNAROUND =seg en q termino - seg de arribo      
                    act[7]= act[6]-act[4]                                               #Guardo el tiempo de espera total, turnaround - tiempo de CPU
                    borrados.append(act)                                                #Guardo el proceso que termino
            else:
                break   #Si el tiempo de arribo es mayor al tiempo actual este y el resto de los procesos en la lista no se deben ejecutar, por lo tanto salgo del ciclo
        for borrar in borrados:
            Procesos.remove(borrar)                                                     #remuevo los procesos que terminaron de la cola en ejecucion
            terminados.append(borrar)                                                   #agrego el proceso a la lista de terminados
    return terminados