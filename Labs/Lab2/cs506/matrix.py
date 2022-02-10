import copy
# import read

def get_determinant(A: list[list]):
    """
    """
    if len(A) != len(A[0]):
        raise ValueError('Matrix must be square')
    
    det, n = 0, len(A)

    if n == 2 and len(A[0]) == 2:
        return A[0][0] * A[1][1] - A[0][1] * A[1][0]

    for i in range(n):
        B = copy.deepcopy(A)
        B = B[1:]

        for j in range(len(B)):
            B[j] = B[j][0:i] + B[j][i + 1:]

        sign = (-1) ** (i % 2)
        det += sign * A[0][i] * get_determinant(B)

    return det
