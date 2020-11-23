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
                
                Procesos.remove(act) #como el elemento a eliminar en FIFO siempre es la primer posicion, corto el ciclo,
                break               #y vuelvo a recorrer desde el siguiente proceso              
            else:
                break


