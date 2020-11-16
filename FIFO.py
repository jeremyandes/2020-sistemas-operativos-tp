from Timer import iniciaTimer
import time

def algoritmo_fifo(Procesos):

    inicio = time.time()
    while Procesos: #mientras la lista no este vacia
        for act in Procesos: #recorro la lista de procesos
            if act[1]<=(time.time()-inicio):                                    #Si el proceso ya esta listo, ejecuto
                iniciaTimer("Se ejecuta el proceso {}".format(act[0]),act[3])   #Si no, vuelvo a recorrer hasta que este listo
                #Falta guardar en archivo de salida
                print("El proceso {} termino de ejecutarse, en el momento {}".format(act[0],time.time()-inicio))
                indice=Procesos.index(act)
                if indice != 0:
                    Procesos.remove(act)
                    act=act(indice-1)
                else:
                    Procesos.remove(act)
                    break
            else:
                break


