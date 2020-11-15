#Ejecucion de los procesos segun algoritmo de planificion: Round Robin, es de tipo apropiativa
from Timer import iniciaTimer
import time

def round_robin(Procesos, quantum):
    inicio=time.time()                                                                  #Guardo el tiempo en el que se empezo a ejecutar el algoritmo
    while Procesos:                                                                     #Mientras la lista de procesos no este vacia
        for act in Procesos:                                                            #Recorro cada proceso en la lista
            if act[1]<= (time.time()-inicio) :                                          #Si el tiempo de arribo es <= al tiempo transcurrido desde que comenzo el algoritmo
                if quantum > act[3] :                                                   #Si el tiempo restante del proceso es menor al quantum
                    iniciaTimer("Se ejecuta el proceso {}". format(act[0]), act[3])     #Entonces pasa por parametro ese tiempo 
                else:
                    iniciaTimer("Se ejecuta el proceso {}". format(act[0]), quantum)    #Sino pasa por parametro el tiempo del quantum
                act[3]-=quantum                                                         #Se resta el valor del quantum ya sea que se halla ejecutado completo o no
                if act[3]<=0 :                                                          #El proceso termino si su tiempo restante es menor o igual a cero
                    #agregar al archivo de salida - falta desarrollar la funcion
                    print("El proceso {} termino de ejecutarse. En el momento {}".format(act[0],time.time()-inicio))#Se imprime por pantalla el proceso que termino
                    Procesos.remove(act)                                                #se remueve el proceso de la lista
            else:
                break   #Si el tiempo de arribo es mayor al tiempo actual este y el resto de los procesos en la lista no se deben ejecutar, por lo tanto salgo del ciclo


