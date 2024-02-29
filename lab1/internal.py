import numpy as np


def make_C_and_D_matrix(A, B):
    matrix = np.hstack((A, B * -1))
    res = np.zeros((0, matrix.shape[1]))
    for index, row in enumerate(matrix):
        tmp = row / row[index]
        tmp[index] = 0
        res = np.vstack((res, tmp))
    res = res * -1
    return res[:, :-1], res[:, -1:]


def check_norma(A: np.ndarray[np.float64]):
    return norma(A) < 1


def norma(A: np.ndarray[np.float64]):
    return max([sum(abs(row)) for row in A])


def sort_diagonal_predominance(A: np.ndarray[np.float64]):
    indeces = []

    strict = False
    for row in A:
        if max(row) >= sum(row) - max(row):
            if max(row) > sum(row) - max(row):
                strict = True
            indeces.append(np.argmax(row))
        else:
            raise ValueError(
                "Невозможно построить матрицу с диагональным преобладанием!"
            )

    uniq = set(indeces)
    if len(uniq) != len(indeces) or not (strict):
        raise ValueError("Невозможно построить матрицу с диагональным преобладанием!")

    A = np.take(A, indeces, axis=1)

    return A


def abs_deviations(k: np.ndarray[np.float64], prev: np.ndarray[np.float64]) -> int:
    return max(abs(k - prev))


def discrepancy():
    return 0


def relative_differences(
    k: np.ndarray[np.float64], prev: np.ndarray[np.float64]
) -> int:
    return max(abs((k - prev) / k))


def iterational_method(C, D: np.ndarray[np.float64], accuracy, max_iter):
    headers = ["x " + str(i) for i in range(0, C.shape[0])]
    headers.append("Критерий по абсолютным отклонениям")
    accuracy_list = [0]
    result_matrix = [D]
    x = D
    for _ in range(max_iter - 1):
        x = C @ x + D
        criteria_abs = abs_deviations(x, result_matrix[-1])
        result_matrix.append(x)
        accuracy_list.append(criteria_abs)
        if criteria_abs <= accuracy:
            res = np.squeeze(np.array(result_matrix))
            result = np.hstack(
                (res, np.array(accuracy_list, dtype=object).reshape(-1, 1))
            )
            return result, headers

    print("Достигли максимального кол-во итераций")

    res = np.squeeze(np.array(result_matrix))
    result = np.hstack((res, np.array(accuracy_list, dtype=object).reshape(-1, 1)))
    return result, headers
