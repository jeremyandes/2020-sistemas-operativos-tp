from termcolor import colored
from Timer import aMinSeg

'''Tiempo de Turnaround de cada proceso_el total transcurrido desde que se inicia (Ti) hasta que finaliza (Tf)
Tiempo de Espera en la Cola de Listos
Tiempo de Espera Total_ turnaround - cola de listos 
Es el tiempo en que los procesos están activos pero sin ser ejecutados, es decir, los tiempos de espera en las distintas colas
Tiempo de Respuesta_Tiempo que pasa desde que se manda ejecutar un proceso hasta que se ejecuta por primera vez.
Tiempo Total de Uso de procesador'''

'''[0]ID [1]TArribo [2]prioridad [3]tiempo de procesador [4]tiempo de CPU [5]tiempo de rta [6]turnaround [7]espera total'''
#Funcion que muestra los resultados de la simulacion por proceso
def muestra_result(terminados, turna, cola, esptot, rta, cpu) : #ingresa por parametro una lista con las carcteristicas definidas arriba ^
    print(colored("RESULTADOS DE LA SIMULACION POR PROCESO", "magenta").center(30, " "))
    print(colored("  proceso  |   turnaround    | cola de listos | espera total |    respuesta    |     uso de CPU     ", "green"))
    for p in terminados :                                       #Muestro los resultados por proceso
        cadena="{:^11s}".format(str(p[0]))                      #inicializo la cadena con el id 
        cadena+="|" + "{:.2f} [s]".format(p[turna]).center(17)  #agrego el tiempo turnaround
        cadena+="|" + "{:.2f} [s]".format(p[cola]).center(16)   #agrego el tiempo de espera en la cola de listos
        cadena+="|" + "{:.2f} [s]".format(p[esptot]).center(14) #agrego el tiempo de espera total
        cadena+="|" + "{:.2f} [s]".format(p[rta]).center(17)    #agrego el tiempo de respuesta
        cadena+="|" + "{:.2f} [s]".format(p[cpu]).center(20)    #agrego el tiempo de uso de CPU
        print(cadena)                                           #imprimo la cadena

def muestra_sisresult(promturna, esptotal) :
    print("\n")
    print(colored("RESULTADOS DE LA SIMULACION A NIVEL SISTEMA", "magenta").center(30, " "))
    print("Tiempo promedio turnaround {:.2f} [s]".format(promturna))
    (min, seg)= aMinSeg(int(esptotal))
    print("Tiempo de espera total de los procesos en el sistema {}:{} [minutos]".format(min, seg))

#Funcion que carga los resultados de ejecuion en un archivo
def escribe_archivo(nomArch, terminados, turna, cola, esptot, rta, cpu) :
    nomArch+=".txt"
    f=open(nomArch, 'w')
    for p in terminados :
        f.write("id: {}".format(str(p[0])))
        f.write("|turnaround: {:.2f} [s]".format(p[turna]))
        f.write("|espera en cola de listos: {:.2f} [s]".format(p[cola]))
        f.write("|espera total: {:.2f} [s]".format(p[esptot]))
        f.write("|respuesta: {:.2f} [s]".format(p[rta]))
        f.write("|uso de CPU: {:.2f} [s]".format(p[cpu]))
        f.write("\n")
    f.close()

#Funcion que evalua el tiempo de Turnaround Promedio de los procesos en el sistema. Se mide en segundos.
def promedio_turnaround(terminados, turna) :
    sum=0
    cont=0
    for p in terminados:
        sum+=p[turna]
        cont+=1
    if cont == 0 :
        return 0
    else :
        return sum/cont

#Tiempo de Espera Total de los procesos en el sistema. Se mide en segundos.
def espera_total(terminados, esp) :
    sum=0
    for p in terminados:
        sum+=p[esp]
    return sum