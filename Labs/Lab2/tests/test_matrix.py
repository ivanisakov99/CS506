import pytest
from cs506 import read, matrix
import numpy as np

@pytest.mark.parametrize('matrixPath', [
    ("tests/test_files/dataset_3_1.csv"),
])
def test_matrix_det_square(matrixPath):
    mat = read.read_csv(matrixPath)
    
    assert round(matrix.get_determinant(mat), 9) == round(np.linalg.det(mat), 9)


@pytest.mark.parametrize('matrixPath', [
    ("tests/test_files/dataset_3_2.csv"),
])
def test_matrix_det_not_square(matrixPath):
    try:
        mat = read.read_csv(matrixPath)
        matrix.get_determinant(mat)
    except ValueError as e:
        assert str(e) == 'Matrix must be square'
