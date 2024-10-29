import numpy as np

def add_matrices(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def subtract_matrices(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def multiply_matrices(A, B):
    # for 2x2
    if len(A) == 2:
        return [
            [
                A[0][0] * B[0][0] + A[0][1] * B[1][0],  # C11
                A[0][0] * B[0][1] + A[0][1] * B[1][1],  # C12
            ],
            [
                A[1][0] * B[0][0] + A[1][1] * B[1][0],  # C21
                A[1][0] * B[0][1] + A[1][1] * B[1][1],  # C22
            ]
        ]

    # Matrices into 2x2 
    mid = len(A) // 2
    A11 = [row[:mid] for row in A[:mid]]
    A12 = [row[mid:] for row in A[:mid]]
    A21 = [row[:mid] for row in A[mid:]]
    A22 = [row[mid:] for row in A[mid:]]

    B11 = [row[:mid] for row in B[:mid]]
    B12 = [row[mid:] for row in B[:mid]]
    B21 = [row[:mid] for row in B[mid:]]
    B22 = [row[mid:] for row in B[mid:]]

    C11 = add_matrices(multiply_matrices(A11, B11), multiply_matrices(A12, B21))
    C12 = add_matrices(multiply_matrices(A11, B12), multiply_matrices(A12, B22))
    C21 = add_matrices(multiply_matrices(A21, B11), multiply_matrices(A22, B21))
    C22 = add_matrices(multiply_matrices(A21, B12), multiply_matrices(A22, B22))

    # Combining
    C = []
    for i in range(len(C11)):
        C.append(C11[i] + C12[i])
    for i in range(len(C21)):
        C.append(C21[i] + C22[i])
    
    return C

A = [
    [1, 9, 3, 4],
    [5, 6, 3, 8],
    [9, 0, 11, 2],
    [13, 4, -5, 3]
]

B = [
    [1, 0, 0, 1],
    [0, 1, 1, 0],
    [1, 1, 0, 0],
    [0, 0, 1, 1]
]

C = multiply_matrices(A, B)
print("C:")
for row in C:
    print(row)
