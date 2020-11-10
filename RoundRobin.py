#Ejecucion de los procesos segun algoritmo de planificion: Round Robin, es de tipo apropiativa
from Timer import iniciaTimer

def round_robin(Procesos, quantum)
    while not Procesos:                                                             #Mientras la lista de procesos no este vacia
        act=Procesos[0]
        if quantum > act[3] :                                                       #Si el tiempo restante del proceso es menor al quantum
            Timer.iniciaTimer("Se ejecuta el proceso {}". format(act[0]), act[3])   #Entonces pasa por parametro ese tiempo 
        else:
            Timer.iniciaTimer("Se ejecuta el proceso {}". format(act[0]), quantum)  #Sino pasa por parametro el tiempo del quantum
        act[3]-=quantum                                                             #Se resta el valor del quantum ya sea que se halla ejecutado completo o no
        Procesos.remove(act)                                                        #se remueve el primer elemento de la lista
        if act[3]<=0 :                                                              #El proceso termino si su tiempo restante es menor o igual a cero
            #agregar al archivo de salida - falta desarrollar la funcion
            print("El proceso {} termino de ejecutarse.".format(act[0]))            #Se imprime por pantalla el ID del proceso que termino
        else:
            Procesos.append(act)                                                    #Se pone el proceso al final de la lista, como si fuera una cola

