#librería con la que se puede realizar muchas operaciones, después la veremos en profundidad, tiene cosas copadas
import operator

#paso lista por parámetro
def OrdenaLlegada(lista):

    #almaceno la lista ordenada por el campo [1] en una variable
    #con el parametro "key" me paro en cada elemento de la lista, y el número es el campo
    listaNueva = sorted(lista, key=operator.itemgetter(1))

    return listaNueva


#dejo las otras funciones por si quieren probarlas, es el mismo procedimiento
def OrdenaID(lista):
    #key con campo [0]
    listaNueva = sorted(lista, key=operator.itemgetter(0))
    return listaNueva

def OrdenaPDP(lista):
    #key con campo [2]
    listaNueva = sorted(lista, key=operator.itemgetter(2))
    return listaNueva

def OrdenaTDP(lista):
    #key con campo [3]
    listaNueva = sorted(lista, key=operator.itemgetter(3))
    return listaNueva