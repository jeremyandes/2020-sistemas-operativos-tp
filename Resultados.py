from termcolor import colored
from Timer import convierteContador
import math

'''Tiempo de Turnaround de cada proceso_el total transcurrido desde que se inicia (Ti) hasta que finaliza (Tf)
Tiempo de Espera en la Cola de Listos
Tiempo de Espera Total_ turnaround - cola de listos 
Es el tiempo en que los procesos están activos pero sin ser ejecutados, es decir, los tiempos de espera en las distintas colas
Tiempo de Respuesta_Tiempo que pasa desde que se manda ejecutar un proceso hasta que se ejecuta por primera vez.
Tiempo Total de Uso de procesador'''

'''[0]ID [1]TArribo [2]prioridad [3]tiempo de procesador [4]tiempo de CPU [5]tiempo de rta [6]turnaround [7]espera total'''
#Funcion que muestra los resultados de la simulacion por proceso
def muestra_result(terminados) : #ingresa por parametro una lista con las carcteristicas definidas arriba ^
    print(colored("RESULTADOS DE LA SIMULACION POR PROCESO", "magenta").center(30, " "))
    print(colored("  proceso  |   turnaround    | cola de listos | espera total |    respuesta    |     uso de CPU     ", "green"))
    for p in terminados :                                       #Muestro los resultados por proceso
        cadena="{:^11s}".format(str(p[0]))                      #inicializo la cadena con el id 
        cadena+="|" + "{:.2f} [s]".format(p[6]).center(17)      #agrego el tiempo turnaround
        cadena+="|" + "{:.2f} [s]".format(p[7]).center(16)      #agrego el tiempo de espera en la cola de listos
        cadena+="|" + "{:.2f} [s]".format(p[7]).center(14)      #agrego el tiempo de espera total
        cadena+="|" + "{:.2f} [s]".format(p[5]).center(17)      #agrego el tiempo de respuesta
        cadena+="|" + "{:.2f} [s]".format(p[4]).center(20)      #agrego el tiempo de uso de CPU
        print(cadena)                                           #imprimo la cadena

#Funcion que muestra los resultados de la simulacion a nivel sistema
def muestra_sisresult(promturna, esptotal, threads, promrta) :
    print("\n")
    print(colored("RESULTADOS DE LA SIMULACION A NIVEL SISTEMA", "magenta").center(30, " "))
    print("Tiempo promedio turnaround {:.2f} [s]".format(promturna))
    print("Tiempo de espera total de los procesos en el sistema {:.2f} [s]".format(esptotal))
    print("Tiempo promedio de respuesta {:.2f} [s]".format(promrta))
    if threads != 1 :                                        #Muestra cantidad de threads utilizados (si corresponde).
        print("Se utilizaron {} threads".format(threads))

#Funcion que carga los resultados de ejecuion en un archivo
def escribe_archivo(nomArch, terminados) :
    nomArch+=".txt"
    f=open(nomArch, 'w')
    for p in terminados :
        f.write("id: {}".format(str(p[0])))
        f.write("|turnaround: {:.2f} [s]".format(p[6]))
        f.write("|espera en cola de listos: {:.2f} [s]".format(p[7]))
        f.write("|espera total: {:.2f} [s]".format(p[7]))
        f.write("|respuesta: {:.2f} [s]".format(p[5]))
        f.write("|uso de CPU: {:.2f} [s]".format(p[4]))
        f.write("\n")
    f.close()

#Funcion que evalua el tiempo de Turnaround Promedio de los procesos en el sistema. Se mide en segundos.
def promedio_turnaround(terminados) :
    sum=0
    cont=0
    for p in terminados:
        sum+=p[6] #posicion que contiene el tiempo turnaround
        cont+=1
    if cont == 0 :
        return 0
    else :
        return sum/cont

#Tiempo de Espera Total de los procesos en el sistema. Se mide en segundos.
def espera_total(terminados) :
    sum=0
    for p in terminados:
        sum+=p[7] #posicion que contiene la espera total
    return sum

#Tiempo de Respuesta Promedio de los procesos en el sistema. Se mide en segundos.
def promedio_respuesta(terminados) :
    sum=0
    cont=0
    for p in terminados:
        sum+=p[5]
        cont+=1
    if cont == 0 :
        return 0
    else :
        return sum/cont

#Cantidad promedio de trabajos finalizados por cada 1000 segundos.
def promedio_trabajos(terminados) :
    milseg=[]                           #inicializo la lista que cuenta los trabajos terminados cada 1000
    seg=[]                              #inicializo la lista que me dice que milisegundos tienen por lo menos un proceso que termino en ellos 
    for p in procesos :
        terminoen= p[6] + p[1]          #segundo de ejecucion del algoritmo en que termino el proceso, turnaround + arribo
        mili=math.ceil(terminoen/1000)  #divide el tiempo en que termino por mil, y redondea hacia arriba
        #1455seg / 1000 =1,455 cuando redodndea queda 2, es decir esta dentro de los 2000 seg
        if mili not in seg :
            seg.append(mili)
            milseg.append(1)
        else :
            milseg[seg.index(mili)]+=1
    #Aca ya tengo la lista milseg, paralela a seg, que contiene todos los contadores por unidad de tiempo (1000 seg)
    sum=0
    for m in milseg:
        sum+=m
    maximo= max()

