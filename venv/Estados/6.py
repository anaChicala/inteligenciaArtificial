import numpy as np

class Nodo:
    def __init__(self, costo, distancia, tupla, tuplaPadre):
        self.costo = costo
        self.distancia = distancia
        self.posicion = tupla
        self.padre = tuplaPadre

    def relacionarlo(self, elementos):
        for elemento in elementos:
            self.relacionCon.append(elemento)

    def setearDistancia(self, distancia):
        self.distancia = distancia;
    def setearCosto(self, costo):
        self.costo = costo;

    def verCosto(self):
        return self.costo
    def verDistancia(self):
        return self.distancia
    def verPadre(self):
        return self.padre
    def verPosicion(self):
        return self.posicion

class Tablero:
    def __init__(self, ancho, largo):
        self.ancho = ancho
        self.largo = largo
        self.board = np.zeros((ancho, largo))

    def definirParedes(self):
        # self.board.itemset((0,0),-1)
        # self.board.itemset((0, 1), -1)
        # self.board.itemset((0, 8), -1)
        # self.board.itemset((1, 0), -1)
        # self.board.itemset((1, 1), -1)
        # self.board.itemset((1, 8), -1)
        # self.board.itemset((3, 0), -1)
        # self.board.itemset((3, 3), -1)
        # self.board.itemset((3, 4), -1)
        # self.board.itemset((3, 5), -1)
        # self.board.itemset((3, 7), -1)
        # self.board.itemset((3, 8), -1)
        # self.board.itemset((4, 5), -1)
        # self.board.itemset((4, 7), -1)
        # self.board.itemset((5, 7), -1)
        # self.board.itemset((6, 2), -1)
        # self.board.itemset((6, 7), -1)
        # self.board.itemset((7, 1), -1)
        # self.board.itemset((7, 2), -1)
        # self.board.itemset((8, 2), -1)
        # self.board.itemset((8, 7), -1)
        # self.board.itemset((8, 8), -1)
        # self.board.itemset((8, 9), -1)

        self.board.itemset((10, 2), -1)
        self.board.itemset((11, 2), -1)
        self.board.itemset((12, 2), -1)
        self.board.itemset((13, 2), -1)
        self.board.itemset((14, 2), -1)
        self.board.itemset((15, 2), -1)
        self.board.itemset((16, 2), -1)
        self.board.itemset((17, 2), -1)
        self.board.itemset((18, 2), -1)
        self.board.itemset((19, 2), -1)
        self.board.itemset((10, 3), -1)
        self.board.itemset((10, 4), -1)
        self.board.itemset((10, 5), -1)
        self.board.itemset((5, 5), -1)
        self.board.itemset((5, 6), -1)
        self.board.itemset((7, 8), -1)
        self.board.itemset((8, 8), -1)
        self.board.itemset((9, 8), -1)
        self.board.itemset((9, 9), -1)

    def verTablero(self):
        return self.board


if __name__ == '__main__':

    # tablero = Tablero(10,10)
    tablero = Tablero(20, 20)
    tablero.definirParedes()
    print(tablero.verTablero())




    # nodoInicial = Nodo(0, 4, (5,4), (5,4))
    # nodoFinal = Nodo(0, 0, (1,4),(1,4))
    nodoInicial = Nodo(0, 16, (15,3), (15,3))
    nodoFinal = Nodo(0, 0, (4,8),(4,8))


    board = tablero.verTablero()
    listaAbierta = [nodoInicial]
    listaCerrada = []

    ok = False
    i = 0
    while ok !=True:

        a = listaAbierta[0]
        listaAbierta.pop(0)
        listaCerrada.append(a)

        adelante = Nodo(0,0, (a.verPosicion()[0] - 1,a.verPosicion()[1] ), a.verPosicion())
        diagonalAdelante1 = Nodo(0,0, (a.verPosicion()[0] - 1,a.verPosicion()[1] - 1 ), a.verPosicion())
        diagonalAdelante2 = Nodo(0,0, (a.verPosicion()[0] - 1,a.verPosicion()[1] + 1), a.verPosicion())
        atras =Nodo(0,0, (a.verPosicion()[0] + 1,a.verPosicion()[1]), a.verPosicion())
        diagonalAtras1 = Nodo(0,0, (a.verPosicion()[0] + 1,a.verPosicion()[1] -1 ), a.verPosicion())
        diagonalAtras2 =Nodo(0,0, (a.verPosicion()[0] + 1,a.verPosicion()[1] +1 ), a.verPosicion())
        ladoIzquierdo = Nodo(0,0, (a.verPosicion()[0] ,a.verPosicion()[1] -1), a.verPosicion())
        ladoDerecho = Nodo(0,0, (a.verPosicion()[0] ,a.verPosicion()[1] +1), a.verPosicion())


        arregloDeNodos = [adelante, diagonalAdelante1,diagonalAdelante2,atras,diagonalAtras1, diagonalAtras2, ladoIzquierdo,ladoDerecho]

        # Se ve si ya se llego a la meta:
        for ele in arregloDeNodos:
            if (ele.verPosicion() == nodoFinal.verPosicion()):
                print("Encontramos el camino")
                a = ele.verPosicion()
                p = ele.verPadre()
                # En caso de que si, se imprime el camino.
                while(ok ==False):

                    print(a)
                    if(a ==nodoInicial.verPosicion()):
                        ok = True
                    else:
                        for ele in listaCerrada:
                            if (ele.verPosicion() == p):
                                p = ele.verPadre()
                                a = ele.verPosicion()



        if(ok == False):
            # Eliminamos de la lista los nodos que corresponden a alguna pared
            index = 0
            for elemento in arregloDeNodos:
                if(elemento.verPosicion()[0]==20 or elemento.verPosicion()[1]==20 ):
                    pass
                else:
                    if (board.item(elemento.verPosicion()) == -1):
                        arregloDeNodos.pop(index)
                index = index + 1

            # Seteamos el costo y la distancia de cada uno de los nodos
            index = 0
            for elemento in arregloDeNodos:
                # print(elemento.verPosicion())
                # print("X Final: ",nodoFinal.verPosicion()[0])
                # print("X Elemento: ",elemento.verPosicion()[0])
                # print("Y Final: ",nodoFinal.verPosicion()[1])
                # print("Y Elemento: ",elemento.verPosicion()[1])

                elemento.setearDistancia((abs((nodoFinal.verPosicion()[0]) - (elemento.verPosicion()[0])) + abs((nodoFinal.verPosicion()[1]) - (elemento.verPosicion()[1]))))
                elemento.setearCosto(i+1)
                print("Costo: ", elemento.verDistancia())
                pass

            for e in arregloDeNodos:
                control = 0
                index = 0
                for e1 in listaAbierta:
                    if(e1.verPosicion() == e.verPosicion()):
                        if ((e1.verCosto()+e1.verDistancia()) > (e.verCosto()+e.verDistancia())):
                            listaAbierta[index] =e
                        control = control +1
                        break
                    index = index+1

                for e2 in listaCerrada:
                    if(e2.verPosicion() ==e.verPosicion()):
                        control = control + 1
                        break
                if(control == 0):
                    listaAbierta.append(e)


            # Ordenamos el arreglo de nodos
            intercambios = True
            numPasada = len(listaAbierta) - 1
            while numPasada > 0 and intercambios:
                intercambios = False
                for j in range(numPasada):
                    costoTotal = listaAbierta[j].verDistancia() + listaAbierta[j].verCosto()
                    # print(costoTotal)
                    if costoTotal > (listaAbierta[j+1].verDistancia() + listaAbierta[j+1].verCosto()):
                        intercambios = True
                        temp = listaAbierta[j]
                        listaAbierta[j] = listaAbierta[j + 1]
                        listaAbierta[j + 1] = temp
                numPasada = numPasada - 1

            # for elemento in listaAbierta:
            #     print(elemento.verCosto()+elemento.verDistancia())


            i = i + 1
            print("Ciclo: ", i+1)
            # listaDelCamino.append(listaAbierta[0])

