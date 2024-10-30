import numpy as np

def add_matrices(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def subtract_matrices(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def strassen_multiply(A, B):
    n = len(A)

    #for 1x1
    if n == 1:
        return [[A[0][0] * B[0][0]]]

    #matrices into quarters
    mid = n // 2
    A11 = [row[:mid] for row in A[:mid]]
    A12 = [row[mid:] for row in A[:mid]]
    A21 = [row[:mid] for row in A[mid:]]
    A22 = [row[mid:] for row in A[mid:]]

    B11 = [row[:mid] for row in B[:mid]]
    B12 = [row[mid:] for row in B[:mid]]
    B21 = [row[:mid] for row in B[mid:]]
    B22 = [row[mid:] for row in B[mid:]]

    P = strassen_multiply(add_matrices(A11, A22), add_matrices(B11, B22))
    Q = strassen_multiply(add_matrices(A21, A22), B11)
    R = strassen_multiply(A11, subtract_matrices(B12, B22))
    S = strassen_multiply(A22, subtract_matrices(B21, B11))
    T = strassen_multiply(add_matrices(A11, A12), B22)
    U = strassen_multiply(subtract_matrices(A21, A11), add_matrices(B11, B12))
    V = strassen_multiply(subtract_matrices(A12, A22), add_matrices(B21, B22))

    # Combine results
    C11 = add_matrices(P, subtract_matrices(add_matrices(S, V), T))
    C12 = add_matrices(R, T)
    C21 = add_matrices(Q, S)
    C22 = subtract_matrices(add_matrices(P, R), add_matrices(Q, U))

    C = []
    for i in range(mid):
        C.append(C11[i] + C12[i])
    for i in range(mid):
        C.append(C21[i] + C22[i])

    return C
A = [
    [8, 4, 2, 5],
    [5, 0, 7, 8],
    [0, 1, 2, 2],
    [3, 0, 1, 4]
]

B = [
    [1, 0, 0, 1],
    [0, 1, 1, 0],
    [1, 1, 0, 0],
    [0, 0, 1, 1]
]

C = strassen_multiply(A, B)
print("C:")
for row in C:
    print(row)
