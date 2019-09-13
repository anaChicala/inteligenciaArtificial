# Con todos los valores NO anda
import numpy as np
arrayPesos = [2, 2, 4, 2.5, 3, 2.5, 2]
salidaEsperada = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
alfa = 0.01
entradas1 = [3, 2, 2, 2, 2, 2, 3]
entradas2 = [1, 2, 1, 1, 1, 1, 1]
entradas3 = [3, 2, 1, 3, 1, 1, 5]
entradas4 = [3, 2, 1, 2, 1, 2, 3]
entradas5 = [1, 2, 2, 2, 5, 1, 1]
entradas6 = [5, 1, 4, 1, 1, 2, 3]
entradas7 = [3, 2, 1, 4, 2, 2, 3]
entradas8 = [5, 1, 1, 1, 1, 1, 1]
entradas9 = [3, 2, 2, 3, 2, 2, 3]
entradas10 = [3, 2, 2, 4, 1, 2, 3]
entradas = [entradas1, entradas2, entradas3, entradas4, entradas5, entradas6, entradas7, entradas8, entradas9, entradas10]
resultado = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
errores = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]



def calculoSalida():

    i = 0
    for entrada in entradas:
        resultado[i] = entrada[0] * arrayPesos[0] + entrada[1] * arrayPesos[1] + entrada[2] * arrayPesos[2] +entrada[3] * arrayPesos[3]+entrada[4] * arrayPesos[4]+entrada[5] * arrayPesos[5]+entrada[6] * arrayPesos[6]


        errores[i] = salidaEsperada[i]-resultado[i]

        calculoPesos(i, entrada)
        i = i+1



    print("Termino un ciclo")

def calculoPesos(i, entrada):
    arrayPesos[0] = arrayPesos[0] + alfa * (salidaEsperada[i] - resultado[i]) * entrada[0]
    arrayPesos[1] = arrayPesos[1] + alfa * (salidaEsperada[i] - resultado[i]) * entrada[1]
    arrayPesos[2] = arrayPesos[2] + alfa * (salidaEsperada[i] - resultado[i]) * entrada[2]
    arrayPesos[3] = arrayPesos[3] + alfa * (salidaEsperada[i] - resultado[i]) * entrada[3]
    arrayPesos[4] = arrayPesos[4] + alfa * (salidaEsperada[i] - resultado[i]) * entrada[4]
    arrayPesos[5] = arrayPesos[5] + alfa * (salidaEsperada[i] - resultado[i]) * entrada[5]
    arrayPesos[6] = arrayPesos[6] + alfa * (salidaEsperada[i] - resultado[i]) * entrada[6]



def controlError(error):
    print("Errores:", errores)
    if( error[0] == 0 and error[1] == 0 and error[2] == 0 and error[3] == 0 and error[4] == 0 and error[5] == 0 and error[6] == 0 and error[7] == 0 and error[8] == 0  and error[9] == 0 ):
        return True
    else:
        return False

if __name__ == '__main__':
    print("Empieza a calcular:");

    ok = False
    j = 0
    while ok !=True:
        calculoSalida()
        ok = controlError(errores)
        j=j+1;
    print("Termino en: ", j)
    print("Los pesos son: ", arrayPesos)
    pass
