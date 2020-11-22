#Ejecucion de los procesos segun algoritmo de planificion: Round Robin, es de tipo apropiativa
from Timer import iniciaTimer
import time
from termcolor import colored

'''Tiempo de Turnaround de cada proceso_el total transcurrido desde que se inicia (Ti) hasta que finaliza (Tf)
Tiempo de Espera en la Cola de Listos
Tiempo de Espera Total_ turnaround - cola de listos 
Es el tiempo en que los procesos están activos pero sin ser ejecutados, es decir, los tiempos de espera en las distintas colas
Tiempo de Respuesta_Tiempo que pasa desde que se manda ejecutar un proceso hasta que se ejecuta por primera vez.
Tiempo Total de Uso de procesador_
[0]ID [1]TArribo [2]prioridad [3]tiempo de procesador [4]tiempo de CPU
[5]tiempo de rta [6]turnaround'''
#Tiempo de espera en cola de listos = es el transcurrido desde Ti hasta que se ejecuta por primera vez ?

def round_robin(Procesos, quantum):
    inicio=time.time()                                                                  #Guardo el tiempo en el que se empezo a ejecutar el algoritmo
    terminados=[]                                                                       #defino la lista de procesos terminados como vacia
    for p in Procesos :
        p.append(0)                                                                     #pongo el tiempo ejecutado en cero
    while Procesos :                                                                    #Mientras la lista de procesos no este vacia
        borrados=[]                                                                     #inicializo la lista de borrados como vacía en el ciclo actual
        for act in Procesos:                                                            #Recorro cada proceso en la lista
            if act[1] <= (time.time()-inicio) :                                         #Si el tiempo de arribo es <= al tiempo transcurrido desde que comenzo el algoritmo
                if act[4] == 0 :                                                        #El proceso llego pero no se ejecuto tdv
                    act.append(time.time()-inicio)                                      #Establezco el tiempo en que se comenzo a ejecutarse el primer quantum
                if quantum > act[3] :                                                   #Si el tiempo restante del proceso es menor al quantum
                    iniciaTimer("Se ejecuta el proceso {}". format(act[0]), act[3])     #Entonces pasa por parametro ese tiempo 
                    act[4]+=act[3]                                                      #se suma el tiempo en procesador
                else:
                    iniciaTimer("Se ejecuta el proceso {}". format(act[0]), quantum)    #Sino pasa por parametro el tiempo del quantum
                    act[4]+=quantum                                                     #se suma el tiempo en procesador
                act[3]-=quantum                                                         #Se resta el valor del quantum ya sea que se halla ejecutado completo o no
                if act[3]<=0 :                                                          #El proceso termino si su tiempo restante es menor o igual a cero
                    #agregar al archivo de salida - falta desarrollar la funcion
                    print("El proceso {} termino de ejecutarse. En el momento {:.1f} \n".format(act[0],time.time()-inicio))#Se imprime por pantalla el proceso que termino
                    act.append(time.time() - inicio - act[1])                           #Guardo el tiempo TURNAROUND =seg en q termino - seg de arribo
                    borrados.append(act)                                                #se remueve el proceso de la lista
            else:
                break   #Si el tiempo de arribo es mayor al tiempo actual este y el resto de los procesos en la lista no se deben ejecutar, por lo tanto salgo del ciclo
        for borrar in borrados:
            Procesos.remove(borrar)                                                     #remuevo los procesos que terminaron de la cola en ejecucion
            terminados.append(borrar)                                                   #agrego el proceso a la lista de terminados
    print(colored("RESULTADOS DE LA SIMULACION POR PROCESO", "magenta").center(20, " "))
    print(colored("  proceso  |   turnaround    | cola de listos | espera total |    respuesta    |     uso de CPU     ", "green"))
    for p in terminados :                                                               #Muestro los resultados por proceso
        print("{:^11s}".format(str(p[0]))+ "|" + "{:.2f} [s]".format(p[6]).center(17) + "|" +"{:.2f} [s]".format(0).center(16)+"|"+ "{:.2f} [s]".format(0).center(14)+"|"+"{:.2f} [s]".format(p[5]).center(17) +"|"+"{:.2f} [s]".format(p[4]).center(20))