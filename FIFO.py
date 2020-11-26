from Timer import minSec
import time
'''
[0]ID [1]TArribo [2]prioridad [3]tiempo de procesador 
[4]tiempo de CPU [5]tiempo de rta [6]turnaround [7]espera total'''

def algoritmo_fifo(Procesos):

    inicio = time.time()
    terminados = list()

    while Procesos: #mientras la lista no este vacia
        
        for act in Procesos: #recorro la lista de procesos
            if act[1]<=(time.time()-inicio):                    #Si el proceso ya esta listo, ejecuto
                                                                #Si no, vuelvo a recorrer hasta que este listo 
                act[5]=(time.time()-inicio-act[1])              #Tiempo de respuesta       
                act[7]=(time.time()-inicio-act[1])              #timepo de espera en la cola
                act[4]=act[3]                                   #tiempo de CPU
                time.sleep(act[3])
                print("[{}]     Proceso ID={} finalizado.\n".format(minSec(int((time.time()-inicio))), act[0]))
                act[6]=(time.time()-inicio-act[1])              #agrego el tiempo de turnarround
                terminados.append(act)                          #guardo en una lista los terminados para tener los resultados
                Procesos.remove(act) #como el elemento a eliminar en FIFO siempre es la primer posicion, corto el ciclo,
                break                #y vuelvo a recorrer desde el siguiente proceso              
            else:
                break                #vuelvo a preguntar si esta listo
    print("EJECUCION FINALIZADA")
    return terminados  #Guardamos en esta lista los procesos finalizados con sus resultados


