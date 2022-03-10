from math import sqrt
from random import normalvariate
from typing import List
import numpy as np

class SVD:
    def __init__(self) -> None:
        pass

    def __randUnitVector(self, N):
        """
        Create a random unit vector

        :param n - Dimension of the vector

        :return random unit vector, 1 x N
        """

        unnormalized = [normalvariate(0, 1) for _ in range(N)]
        theNorm = sqrt(sum(x * x for x in unnormalized))
        return [x / theNorm for x in unnormalized]

    def __svd_1D(self, X: np.ndarray, epsilon = 1e-10):
        """
        Do SVD on one dimension

        :param X - The ndarray to do the SVD on
        :param epsilon - 


        """

        m, n = X.shape
        unit_v = self.__randUnitVector(min(m, n))
        prevVec, currentVec = None, unit_v

        if(m < n):
            A = X @ X.T
        else:
            A = X.T @ X
        
        while(True):
            prevVec = currentVec
            currentVec = A @ currentVec
            currentVec /= np.linalg.norm(currentVec)

            # if(abs(np.dot()) <)


    

    def fit(X: np.ndarray | List[List], k = None):
        """
        Compute the SVD of a matrix X using the 'power method'.

        ---
        :param X: Input matrix
        :param k: The number of singular values to compute. If 'None' the full-rank decompositon is done.
        ---
        :return U, ∑, V: The decomposition
        """

        m, n = X.shape
        rank = min(m, n)


if __name__ == '__main__':
    pass