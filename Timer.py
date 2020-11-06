import time

# texto previo al contador como parámetro
# contador tiene que ser en SEGUNDOS
def iniciaTimer(texto,contador):

    # mientras que el contador no sea 0
    while contador:
        # divmod = hace una división entre (contador,60) y devuelve (mins, secs)
        mins, secs = divmod(contador,60)
        #constructor: primero el texto, despues minutos y segundos formateado a enteros de 2 cifras
        temporizador = "{}    {:02d}:{:02d}".format(texto,mins,secs)
        # "end=\r" : en el output de la terminal, retrocede a la línea anterior y la sobreescribe con un nuevo "print, simulando el contador y evitando imprimir líneas nuevas por cada segundo restado"
        print(temporizador, end="\r")
        # stand by de 1 segundo
        time.sleep(1)
        # resta 1 segundo
        contador -= 1
    print("\n")
