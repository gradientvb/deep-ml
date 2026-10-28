import numpy as np

def transpose_matrix(a: list[list[int | float]]) -> list[list[int | float]]:
    # zip(*a) groups the i-th element of every row together,
    # which is exactly the i-th column
    return [list(col) for col in zip(*a)]

# Equivalent NumPy version:
def transpose_numpy(a):
    return np.array(a).T.tolist()