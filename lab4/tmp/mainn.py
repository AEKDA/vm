import numpy as np


def solve(s, q, A, B):
    solution = np.linalg.solve(A, B)
    print("Невозможно составить матрицу с диагональным перобаладанием")

    return solution
