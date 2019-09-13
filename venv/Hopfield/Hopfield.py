
import numpy as np

# Patron parecido a la T
patronDePrueba = np.array([
        [1, 1, -1, -1, -1, -1, -1, -1, -1, -1,
         1, 1, -1, -1, -1, -1, -1, -1, -1, -1,
         1, 1, -1, -1, -1, -1, -1, -1, -1, -1,
         1, 1, -1, -1, -1, 1, -1, 1, 1, -1,
         1, 1, 1, 1, 1, -1, 1, -1, -1, 1,
         1, 1, 1, 1, 1, -1, 1, -1, -1, 1,
         1, 1, -1, -1, -1, 1, -1, 1, 1, -1,
         1, 1, -1, -1, -1, -1, -1, -1, -1, -1,
         1, 1, -1, -1, -1, -1, -1, -1, -1, -1,
         1, 1, -1, -1, -1, -1, -1, -1, -1, -1]])

# Patron parecido a C
# patronDePrueba = np.array([[
#             1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
#             1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
#             1, 1, -1, -1, -1, -1, -1, -1, 1, 1,
#             1, 1, -1, -1, -1, -1, -1, -1, 1, 1,
#             1, 1, -1, -1, -1, -1, -1, -1, 1, 1,
#             1, 1, -1, -1, -1, -1, -1, -1, 1, 1,
#             1, 1, -1, -1, -1, -1, -1, -1, 1, 1,
#             1, 1, -1, -1, -1, -1, -1, -1, 1, 1,
#             -1, 1, -1, -1, 1, 1, -1, -1, -1, -1,
#             -1, 1, -1, -1, -1, -1, -1, 1, 1, -1]])

t = np.array([
        [1, 1, -1, -1, -1, -1, -1, -1, -1, -1,
         1, 1, -1, -1, -1, -1, -1, -1, -1, -1,
         1, 1, -1, -1, -1, -1, -1, -1, -1, -1,
         1, 1, -1, -1, -1, -1, -1, -1, -1, -1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, -1, -1, -1, -1, -1, -1, -1, -1,
         1, 1, -1, -1, -1, -1, -1, -1, -1, -1,
         1, 1, -1, -1, -1, -1, -1, -1, -1, -1,
         1, 1, -1, -1, -1, -1, -1, -1, -1, -1]])

c = np.array([[
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
            1, 1, -1, -1, -1, -1, -1, -1, 1, 1,
            1, 1, -1, -1, -1, -1, -1, -1, 1, 1,
            1, 1, -1, -1, -1, -1, -1, -1, 1, 1,
            1, 1, -1, -1, -1, -1, -1, -1, 1, 1,
            1, 1, -1, -1, -1, -1, -1, -1, 1, 1,
            1, 1, -1, -1, -1, -1, -1, -1, 1, 1,
            1, 1, -1, -1, -1, -1, -1, -1, 1, 1,
            1, 1, -1, -1, -1, -1, -1, -1, 1, 1]])


matrizDePesosTotal = np.zeros((100,100)) #Se usa para los dos metodos
i = np.eye(100)  #Para el metodo de Hebb

respuestaMulti = np.zeros((1,100))

def calculoMatrizPesosHebb(matrices): #Calculo de la matriz de pesos con Hebb

    respuestaFinalSumaPesosTotales = np.zeros((100, 100))
    global matrizDePesosTotal
    for i in range(len(matrices)):
        respuesta = np.multiply(matrices[i], matrices[i].T)
        respuesta2 = np.subtract(respuesta, i)
        respuestaFinalSumaPesosTotales = np.add(respuestaFinalSumaPesosTotales, respuesta2)
        pass



    matrizDePesosTotal = respuestaFinalSumaPesosTotales
    pass
def calculoMatrizPesosPseudoinversa(matrices): #Calculo de la matriz de pesos con Pseudoinversa

    respuestaFinalSumaPesosTotales = matrices[0]

    global matrizDePesosTotal

    for i in range(len(matrices)):
        if(not i==0):
            respuestaFinalSumaPesosTotales=np.append(respuestaFinalSumaPesosTotales, matrices[i], 0)
        pass

    respuestaFinalSumaPesosTotales= respuestaFinalSumaPesosTotales.T

    respuestaFinalSumaPesosTotalesPseudoInversa= np.linalg.pinv(respuestaFinalSumaPesosTotales)

    matrizDePesosTotal= np.dot(respuestaFinalSumaPesosTotales,respuestaFinalSumaPesosTotalesPseudoInversa)



    # print("Final: ")
    # print(matrizDePesosTotal)
    # print("Matriz de orden: ", matrizDePesosTotal.shape)

    pass




def calculoDelPatron(matriz): #Multiplicacion del patron por la matriz de peso


    global respuestaMulti

    respuestaMulti = np.dot(matriz, matrizDePesosTotal);
    # print(respuestaMulti.shape)


    contador = 0
    for x in np.nditer(respuestaMulti):
        if(x > 0):
            respuestaMulti[0, contador] = 1

        else:
            respuestaMulti[0, contador] = -1

        contador = contador+1



def compararEntreLosPatrones(): #Metodo para comparar si el patron encontrado corresponde a alguno de los almacenados

    if((t == respuestaMulti).all()):
        return 1
    elif((c == respuestaMulti).all()):
        return 2
    else:
        return 0
    pass

def compararEntradaConSalida(matriz): #Metodo para ver si se llego a un estado de equilibrio
    if ((matriz== respuestaMulti).all()):
        print("Entrada igual a salida")
        control = compararEntreLosPatrones()
        return control
    else:
        print("Entrada NO es igual a salida")
        print("Transformacion luego de una vuelta:")
        print(respuestaMulti)
        return 0
    pass


if __name__ == '__main__':

    opcion = input("Que metodo quiere utilizar: 1)Hebb 2)Pseudoinversa? ")

    calculoMatrizPesosPseudoinversa([t, c])

    if(opcion == "1"):

        print("El patron a ingresar es: ")
        print(patronDePrueba)

        print("En base al patron que tengo, averiguo a que patron guardado pertenece")
        calculoDelPatron(patronDePrueba)
        control = compararEntradaConSalida(patronDePrueba)
        contador2 = 0

        while(control == 0):
            print("Ciclo: ", contador2)
            matrizAnterior = respuestaMulti
            calculoDelPatron(respuestaMulti)
            control = compararEntradaConSalida(matrizAnterior)
            contador2 = contador2 + 1
            if(control > 0):
                if(control ==1):
                    print("Coincide con el patron T")
                elif(control==2):
                    print("Coincide con el patron C")
        pass
    elif (opcion =="2"):


        print("El patron a ingresar es: ")
        print(patronDePrueba)

        print("En base al patron que tengo, averiguo a que patron guardado pertenece")
        calculoDelPatron(patronDePrueba)
        control = compararEntradaConSalida(patronDePrueba)
        contador2 = 1

        while (control == 0):
            print("Ciclo: ", contador2)
            matrizAnterior = respuestaMulti
            calculoDelPatron(respuestaMulti)
            control = compararEntradaConSalida(matrizAnterior)
            contador2 = contador2 + 1
            if (control > 0):
                if (control == 1):
                    print("Coincide con el patron T")
                elif (control == 2):
                    print("Coincide con el patron C")
        pass

    else:
        print("No ha ingresado una opcion valida")


#
# ej1 = np.array([[
#     1,-1,-1,1
# ]])
#
#
# ej2 = np.array([[
#     -1,1,1,-1
# ]])
# i2 = np.array([[1, 0, 0, 0],
#               [0, 1, 0, 0],
#               [0, 0, 1, 0],
#               [0, 0, 0, 1]]
#             )