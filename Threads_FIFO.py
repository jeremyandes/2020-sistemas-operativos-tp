import threading
import time

def CreaThreads (cant_threads,Procesos):

    threads = list() 

    for i in range(cant_threads): #creo los threads
        t = threading.Thread(target=threader, args(Procesos,)) 
        threads.append(t)

    



def threader (cola):
    proceso = cola.pop(0)
    time.sleep(proceso[3])





    
