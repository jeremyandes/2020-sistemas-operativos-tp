import threading
import time
'''with some_lock:
    # do something...'''

'''
[0]ID [1]TArribo [2]prioridad [3]tiempo de procesador 
[4]tiempo de CPU [5]tiempo de rta [6]turnaround [7]espera total'''

# esto es para prevenir la condición de carrera
lista_lock = threading.Lock()
print_lock = threading.Lock()
terminados_lock = threading.Lock()

terminados = list()

def threader(Procesos):
    inicio = time.time()

    while Procesos: 
        if Procesos[0][1] <= time.time()-inicio:
            with lista_lock :
                proceso = Procesos.pop(0)
            
            proceso[4] = proceso[3]                         #tiempo de CPU
            proceso[5] = time.time()-inicio-proceso[1]      #tiempo de rta
            proceso[7] = time.time()-inicio-proceso[1]      #timepo de espera
            time.sleep(proceso[3])
            
            with print_lock :
                print("El proceso {} termino de ejecutarse, en el momento {:.2f}".format(proceso[0],time.time()-inicio))
            proceso[6]= time.time()-inicio-proceso[1]      #timepo de turnaround 
        
            with terminados_lock:
                terminados.append(proceso)



def CreaThreads(cant_threads,Procesos):
    threads = list() 
    for i in range(cant_threads): #creo los threads
        #t = threading.Thread(target=threader, args=(tgtHost,))
        t = threading.Thread(target=threader, args=(Procesos,)) 
        threads.append(t)
        t.start()
    for thread in threads :
        thread.join()
    return terminados