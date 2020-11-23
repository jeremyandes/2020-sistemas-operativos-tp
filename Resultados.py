from termcolor import colored

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
    for p in terminados :                                                               #Muestro los resultados por proceso
        print("{:^11s}".format(str(p[0]))+ "|" + "{:.2f} [s]".format(p[6]).center(17) 
        + "|" +"{:.2f} [s]".format(p[5]).center(16)+"|"+ "{:.2f} [s]".format(p[7]).center(14)+"|" #faltan definir tiempos de espera en cola de listos y tiempo de espera total
        +"{:.2f} [s]".format(p[5]).center(17) +"|"+"{:.2f} [s]".format(p[4]).center(20))
