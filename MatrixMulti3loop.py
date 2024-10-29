matrix_A = [[7, -5], [0, 1]]
matrix_B = [[6, 2], [4, 3]]

C = [[0, 0], [0, 0]]
for i in range(len(matrix_A)):
    for j in range(len(matrix_B)):  
        for k in range(len(matrix_B)):
            C[i][j] += matrix_A[i][k] * matrix_B[k][j]
for row in C:
    print(row)