from termcolor import colored
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
    print(colored("RESULTADOS DE LA SIMULACION POR PROCESO", "magenta").center(90))
    print(colored("  proceso  |   turnaround    | cola de listos | espera total |    respuesta    |     uso de CPU     ", "green"))
    for p in terminados :                                       #Muestro los resultados por proceso
        cadena="{:^11s}".format(str(p[0]))                      #inicializo la cadena con el id 
        cadena+="|" + "{:.2f} [s]".format(int(p[6])).center(17)      #agrego el tiempo turnaround
        cadena+="|" + "{:.2f} [s]".format(int(p[7])).center(16)      #agrego el tiempo de espera en la cola de listos
        cadena+="|" + "{:.2f} [s]".format(int(p[7])).center(14)      #agrego el tiempo de espera total
        cadena+="|" + "{:.2f} [s]".format(int(p[5])).center(17)      #agrego el tiempo de respuesta
        cadena+="|" + "{:.2f} [s]".format(int(p[4])).center(20)      #agrego el tiempo de uso de CPU
        print(cadena)                                           #imprimo la cadena
    print("\n")

#Funcion que muestra los resultados de la simulacion a nivel sistema
def muestra_sisresult(promturna, esptotal, threads, promrta, promjob) :
    print(colored("RESULTADOS DE LA SIMULACION A NIVEL SISTEMA", "magenta").center(70))
    print(colored("Tiempo promedio turnaround","green").center(49)+"|"+"{:.2f} [s]".format(promturna).center(17)+"|")
    print(colored("Tiempo de espera total de los procesos","green").center(49)+"|"+"{:.2f} [s]".format(int(esptotal)).center(17)+"|")
    print(colored("Tiempo promedio de respuesta","green").center(49)+"|"+" {:.2f} [s]".format(promrta).center(17)+"|")
    if threads != 1 :                                        #Muestra cantidad de threads utilizados (si corresponde).
        print(colored("Cantidad de threads utilizados","green").center(49)+"|"+"{} ".format(threads).center(17)+"|")
    print(colored("Promedio de trabajos realizados/1000s","green").center(49)+"|"+"{:.2f} [trabajos]".format(promjob).center(17)+"|")
    print("\n")

#Funcion que carga los resultados de ejecuion en un archivo
def escribe_archivo(nomArch, terminados, promturna, esptotal, threads, promrta, promjob) :
    nomArch+=".txt"
    f=open(nomArch, 'w')
    for p in terminados :
        f.write("id: {}".format(str(p[0])))
        f.write("|turnaround: {:.2f} [s]".format(int(p[6])))
        f.write("|espera en cola de listos: {:.2f} [s]".format(int(p[7])))
        f.write("|espera total: {:.2f} [s]".format(int(p[7])))
        f.write("|respuesta: {:.2f} [s]".format(int(p[5])))
        f.write("|uso de CPU: {:.2f} [s]".format(int(p[4])))
        f.write("\n")
    cadena="Pomedio turnaround: {:.2f} [s]".format(promturna)
    cadena+="|Espera total: {:.2f} [s]".format(int(esptotal))
    if threads != 1:
        cadena+="|Cantidad threads: {}".format(threads)
    cadena+="|Promedio respuesta: {:.2f} [s]".format(promrta)
    cadena+="|Promedio trabajos/1000s: {:.2f}".format(promjob)
    f.write(cadena)
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
    max = 0 
    cont = 0
    for p in terminados:    #busco el maximo tiempo absoluto de un proceso en el algoritmo
        t=p[6]+p[1]         #tiempo absoluto del proceso, turnaround + arribo
        cont+=1             #cuento los procesos terminados
        if t > max :
            max=t
    max=math.ceil(max/1000) #si es 7455, por ejemplo, almaceno 8
    if cont == 0 :
        return 0
    else :
        return cont/max