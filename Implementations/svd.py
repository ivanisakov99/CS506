import numpy as np


def svd(X: np.ndarray):
    """
    """

    m, n = X.shape
    rank = min(m, n)

    



def svd_1D(X: np.ndarray, epsilon = 1e-10):
    """
    """

    m, n = X.shape
    unit_v = randUnitV(min(m, n))
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


def randUnitV(n):
    """
    """

    a = np.random.rand(2)
    b = np.random.rand(2)

    print(a, b)
    

if __name__ == '__main__':
    randUnitV(0)