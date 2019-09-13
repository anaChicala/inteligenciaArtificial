
import numpy as np
arrayPesos = [1.5, 0.5, 1.5, 0.5]
salidaEsperada = [0, 0, 0, 1, 0, 1, 1, 1]
alfa = 1
entradas1 = [1, 0, 0, 0]
entradas2 = [1, 1, 0, 0]
entradas3 = [1, 0, 1, 0]
entradas4 = [1, 1, 1, 0]
entradas5 = [1, 0, 0, 1]
entradas6 = [1, 1, 0, 1]
entradas7 = [1, 0, 1, 1]
entradas8 = [1, 1, 1, 1]
entradas = [entradas1, entradas2, entradas3, entradas4, entradas5, entradas6, entradas7, entradas8];
resultado = [0, 0, 0, 0, 0, 0, 0, 0]
errores = [1, 1, 1, 1, 1, 1, 1, 1]



def calculoSalida():

    i = 0
    for entrada in entradas:
        resultado[i] = entrada[0] * arrayPesos[0] + entrada[1] * arrayPesos[1] + entrada[2] * arrayPesos[2] +entrada[3] * arrayPesos[3]
        if (resultado[i] > 0):
            resultado[i] = 1
        else:
            resultado[i] = 0

        errores[i] = salidaEsperada[i]-resultado[i];

        calculoPesos(i, entrada)
        i = i+1

    print("Termino un ciclo")

def calculoPesos(i, entrada):
    arrayPesos[0] = arrayPesos[0] + alfa * (salidaEsperada[i] - resultado[i]) * entrada[0]
    arrayPesos[1] = arrayPesos[1] + alfa * (salidaEsperada[i] - resultado[i]) * entrada[1]
    arrayPesos[2] = arrayPesos[2] + alfa * (salidaEsperada[i] - resultado[i]) * entrada[2]
    arrayPesos[3] = arrayPesos[3] + alfa * (salidaEsperada[i] - resultado[i]) * entrada[3]


def controlError(error):
    print("Errores:", errores)
    if( error[0] == 0 and error[1] == 0 and error[2] == 0 and error[3] == 0 and error[4] == 0 and error[5] == 0 and error[6] == 0 and error[7] == 0  ):
        return True
    else:
        return False

if __name__ == '__main__':
    print("Empieza a calcular:");

    ok = False
    while ok !=True:
        calculoSalida()
        ok = controlError(errores)

    print("Termino")
    print("Los pesos son: ", arrayPesos)
    pass
