#clase "Proceso"
#campo = "valor posible" // pID = >1 && <9999 // tda = >0 && <99999 segundos // pdp = >1 && <15 // tdp = >0 && <9999 segundos
class Proceso:
    def __init__(self, campo, pID, tda, pdp, tdp):
        self.campo = campo
        self.pID = pID
        self.tda = tda
        self.pdp = pdp
        self.tdp = tdp
    def muestra(self):
        return '{}, {}, {}, {}, {}'.format(self.campo,self.pID,self.tda,self.pdp,self.tdp)

proceso1 = Proceso('Campo1', 2500, 10, 12, 1)

print('Campo: {}, pID: {}, tda: {}, pdp: {}, tdp: {}'.format(proceso1.campo, proceso1.pID, proceso1.tda, proceso1.pdp, proceso1.tdp))