from Timer import iniciaTimer
import time
'''
[0]ID [1]TArribo [2]prioridad [3]tiempo de procesador [4]tiempo de CPU
[5]tiempo de rta [6]espera total [7]turnaround'''

def algoritmo_fifo(Procesos):

    inicio = time.time()
    for aux in Procesos:                    #inicializo el tiempo de CPU en cero
        aux.append(0)
    while Procesos: #mientras la lista no este vacia
        terminados = list()
        for act in Procesos: #recorro la lista de procesos
            if act[1]<=(time.time()-inicio):                    #Si el proceso ya esta listo, ejecuto
                                                                #Si no, vuelvo a recorrer hasta que este listo 
                act.append(time.time()-inicio)                  #Tiempo de respuesta       
                act.append(time.time()-inicio-act[1])           #timepo de espera en la cola
                act[4]+=act[3]                                  #Tiempo de CPU
                iniciaTimer("Se ejecuta el proceso {}".format(act[0]),act[3])   
                print("El proceso {} termino de ejecutarse, en el momento {}".format(act[0],time.time()-inicio))
                act.append(time.time()-inicio)                  #agrego el tiempo de turnarround
                terminados.append(act)                          #guardo en una lista los terminados para tener los resultados
                Procesos.remove(act) #como el elemento a eliminar en FIFO siempre es la primer posicion, corto el ciclo,
                break                #y vuelvo a recorrer desde el siguiente proceso              
            else:
                break                #vuelvo a preguntar si esta listo
    return terminados


