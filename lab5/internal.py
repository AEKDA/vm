import util
import numpy as np
import math
from itertools import zip_longest


def finite_differences(points: list):
    headers = ["№", "xi", "yi", *[f"∆{i+1}yi" for i in range(len(points) // 2 - 1)]]

    data = []

    for i in range(len(points) // 2):
        if i == 0:
            data.append([points[i] for i in range(0, len(points), 2)])
            data.append([points[i] for i in range(1, len(points), 2)])
            continue

        tmp = []

        for j in range(len(points) // 2 - i):
            tmp.append(data[-1][j + 1] - data[-1][j])
            pass
        data.append(tmp)

    transposed = list(map(list, zip_longest(*data, fillvalue=None)))
    print("Таблица конечных разностей")
    util.print_table(transposed, headers)

    pass


def interpolate_lagrange(x, y, x_cur):
    res = 0.0
    for i in range(0, len(x)):
        p = 1.0
        for j in range(0, len(x)):
            if i != j:
                p *= (x_cur - x[j]) / (x[i] - x[j])
        res += p * y[i]
    return res


def coef(y, n, i):
    if n == 0:
        return y[i + 1] - y[i]
    return coef(y, n - 1, i + 1) - coef(y, n - 1, i)


def newton_forward_interpolation(x, y, x_cur):
    i = 0
    n = len(x) - 1
    t = (x_cur - x[i]) / (x[1] - x[0])
    print(f"t = {t}")
    return y[i] + sum(
        np.prod([t - j for j in range(k)]) / math.factorial(k) * coef(y, k - 1, i)
        for k in range(1, n - i + 1)
    )


def newton_backward_interpolation(x, y, x_cur):
    n = len(x) - 1
    t = (x_cur - x[n]) / (x[1] - x[0])
    print(f"t = {t}")
    return y[n] + sum(
        np.prod([t + j for j in range(k)]) / math.factorial(k) * coef(y, k - 1, n - k)
        for k in range(1, n + 1)
    )


def interpolate_newton_equal_diff(x, y, x_cur):

    if x_cur > (x[-1] + x[0]) / 2:
        print("интерполяция назад")
        return newton_backward_interpolation(x, y, x_cur), newton_backward_interpolation
    else:
        print("интерполяция вперед")
        return newton_forward_interpolation(x, y, x_cur), newton_forward_interpolation


def poly_newton_coefficient(x_arr, y_arr):
    m = len(x_arr)
    x_arr = np.copy(x_arr)
    a = np.copy(y_arr)
    for k in range(1, m):
        a[k:m] = (a[k:m] - a[k - 1]) / (x_arr[k:m] - x_arr[k - 1])
    return a


def interpolate_newton_sep_diff(x_arr, y_arr, arg):
    newton_sep_diff = 0
    a = poly_newton_coefficient(x_arr, y_arr)
    temp = 1
    p = a[0]
    for i in range(1, len(x_arr)):
        temp *= arg - x_arr[i - 1]
        p += a[i] * temp
    newton_sep_diff = p
    return newton_sep_diff


def check_equals(x_arr, h):
    for i in range(len(x_arr) - 1):
        if round(x_arr[i + 1] - x_arr[i], 4) - h > 0.00001:
            return False
    return True
