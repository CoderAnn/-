import numpy as np
with open('01-Data/matrixA.txt', 'r') as f1:
    with open('01-Data/matrixB.txt', 'r') as f2:
        matrix1 = [int(i) for i in f1.read().split(',')]
        matrix2 = []
        for i in f2.readlines():
            matrix2.append([int(j) for j in i.split(',')])
        results = sorted(np.dot(np.array(matrix1), np.array(matrix2)))
        with open('ans_one.txt', 'w') as f3:
            results = [str(i) for i in results]
            f3.write(' '.join(results))

