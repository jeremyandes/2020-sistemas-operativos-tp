import threading
import time
'''with some_lock:
    # do something...'''

# esto es para prevenir la condición de carrera
lista_lock = threading.Lock()
print_lock = threading.Lock()

def threader (Procesos):
    inicio = time.time()
    with lista_lock :
        proceso = Procesos.pop(0)
    time.sleep(proceso[3])
    with print_lock :
        print("El proceso {} termino de ejecutarse, en el momento {:.2f}".format(proceso,time.time()-inicio))


def CreaThreads (cant_threads,Procesos):

    threads = list() 
    for i in range(cant_threads): #creo los threads
        t = threading.Thread(target=threader, args(Procesos)) 
        threads.append(t)
        t.start()
    for thread in threads :
        thread.join()