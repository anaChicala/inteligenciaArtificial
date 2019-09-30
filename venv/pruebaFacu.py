import sys
import numpy as np


def main2():
    print("Entra")
    inputs = [1, 0, 0, 0, 1, 0, 1, 0,
              1, 1, 0, 0, 0, 0, 0, 1,
              1, 1, 0, 0, 0, 0, 1, 0,
              1, 1, 0, 0, 0, 1, 0, 0,
              1, 0, 1, 0, 0, 0, 0, 1,
              1, 0, 1, 0, 0, 0, 1, 0,
              1, 0, 1, 0, 0, 1, 0, 0,
              1, 0, 0, 1, 0, 0, 0, 1,
              1, 0, 0, 1, 0, 0, 1, 0,
              1, 0, 0, 1, 0, 1, 0, 0]

    expectedOutputs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    weights = [2, 2, 4, 2.5, 3, 2.5, 2, 3]
    alpha = 0.5
    result = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    error = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    whi = True

    while (whi):
        i = 0
        for i in range(10):
            result[i] = (inputs[i * 8] * weights[0]) + (inputs[i * 8 + 1] * weights[1]) + (
                        inputs[i * 8 + 2] * weights[2]) + (inputs[i * 8 + 3] * weights[3]) + (
                                    inputs[i * 8 + 4] * weights[4]) + (inputs[i * 8 + 5] * weights[5]) + (
                                    inputs[i * 8 + 6] * weights[6]) + (inputs[i * 8 + 7] * weights[7])
            # print(inputs[0][5])
            error[i] = expectedOutputs[i] - result[i]
            weights[0] = weights[0] + alpha * (expectedOutputs[i] - result[i]) * inputs[i * 8]
            weights[1] = weights[1] + alpha * (expectedOutputs[i] - result[i]) * inputs[i * 8 + 1]
            weights[2] = weights[2] + alpha * (expectedOutputs[i] - result[i]) * inputs[i * 8 + 2]
            weights[3] = weights[3] + alpha * (expectedOutputs[i] - result[i]) * inputs[i * 8 + 3]
            weights[4] = weights[4] + alpha * (expectedOutputs[i] - result[i]) * inputs[i * 8 + 4]
            weights[5] = weights[5] + alpha * (expectedOutputs[i] - result[i]) * inputs[i * 8 + 5]
            weights[6] = weights[6] + alpha * (expectedOutputs[i] - result[i]) * inputs[i * 8 + 6]
            weights[7] = weights[7] + alpha * (expectedOutputs[i] - result[i]) * inputs[i * 8 + 7]
            print('peso  w1:', weights[0])
            print('peso  w2:', weights[1])
            print('peso  w3:', weights[2])
            print('peso  w4:', weights[3])
            print('peso  w5:', weights[4])
            print('peso  w6:', weights[5])
            print('peso  w7:', weights[6])
            print('peso  w8:', weights[7])
            print('error: ', error)
            print('iteracion: ', i)

        if (error[0] == 0 and error[1] == 0 and error[2] == 0 and error[3] == 0 and error[4] == 0 and error[5] == 0 and
                error[6] == 0 and error[7] == 0 and error[8] == 0 and error[9] == 0):
            print('peso final w1:', weights[0])
            print('peso final w2:', weights[1])
            print('peso final w3:', weights[2])
            print('peso final w4:', weights[3])
            print('peso final w5:', weights[4])
            print('peso final w6:', weights[5])
            print('peso final w7:', weights[6])
            print('peso final w8:', weights[7])
            whi = False;
            if (whi == False):
                break

    return 0

if __name__ == '__main__':
    main2()
    pass
