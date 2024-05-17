import numpy as np
import util
from tmp.mainn import solve


def printer(name, cff, e, s, phi, sigma, r_2):
    print("\n", f"Апроксимация к {name}")
    print("Коэффициенты функции", cff)
    print("Отклонения E:", e)
    print("Мера отклонения S:", s)
    print("Значения функции:", phi)
    print("Значение среднеквадратичного отклонения:", sigma)
    print("Коэффициент детерминации:", r_2)
    pass


def linear_approx(x_arr, y_arr):
    sx = np.sum(x_arr)
    sxx = np.sum(x_arr**2)
    sy = np.sum(y_arr)
    sxy = np.sum(y_arr * x_arr)
    A = []
    B = []
    temp = [sxx, sx]
    A.append(temp)
    B.append(sxy)
    A.append([sx, len(x_arr)])
    B.append(sy)

    print(A)
    print(B)

    return solve(2, 0.001, A, B)


def square_approx(x_arr, y_arr, number_of_coeffs):
    A = []
    B = []
    for i in range(number_of_coeffs):
        temp = []
        b = 0
        for j in range(number_of_coeffs):
            if i == 0 and j == 0:
                temp.append(len(x_arr))
            else:
                temp.append(np.sum(x_arr ** (i + j)))
        for j in range(len(y_arr)):
            b += y_arr[j] * x_arr[j] ** (i)

        B.append(b)
        A.append(temp)
    print(A)
    print(B)
    return solve(number_of_coeffs, 0.001, A, B)


def to_linear(x_arr, y_arr):
    cff = linear_approx(x_arr, y_arr)
    func = lambda x: cff[0] * x + cff[1]
    func_str = f"{cff[0]} * x + {cff[1]}"
    name = "Линейная функция"

    e = count_e(func, x_arr, y_arr)
    s = count_s(e)
    phi = count_phi(func, x_arr)
    sigma = count_sigma(s, len(x_arr))
    r2 = count_r_2(y_arr, phi)

    # util.make_grafic(func, name, func_str, x_arr, y_arr)
    printer(name, cff, e, s, phi, sigma, r2)

    return sigma, func, name, func_str


def to_second_degree(x_arr, y_arr):
    cff = np.flip(square_approx(x_arr, y_arr, 3))
    func = lambda x: cff[0] * x**2 + cff[1] * x + cff[2]
    func_str = f"{cff[0]} * x^2 + {cff[1]} * x + {cff[2]}"
    name = "Полиномиальная функция 2-й степени"

    e = count_e(func, x_arr, y_arr)
    s = count_s(e)
    phi = count_phi(func, x_arr)
    sigma = count_sigma(s, len(x_arr))
    r2 = count_r_2(y_arr, phi)

    # util.make_grafic(func, name, func_str, x_arr, y_arr)
    printer(name, cff, e, s, phi, sigma, r2)

    return sigma, func, name, func_str


def to_third_degree(x_arr, y_arr):
    cff = np.flip(square_approx(x_arr, y_arr, 4))
    func = lambda x: cff[0] * x**3 + cff[1] * x**2 + cff[2] * x + cff[3]
    func_str = f"{round(cff[0], 4)} * x^3 + {round(cff[1], 4)} * x^2 + {round(cff[2], 4)} * x + {round(cff[3], 4)}"
    name = "Полиномиальная функция 3й степени"

    e = count_e(func, x_arr, y_arr)
    s = count_s(e)
    phi = count_phi(func, x_arr)
    sigma = count_sigma(s, len(x_arr))
    r2 = count_r_2(y_arr, phi)

    # util.make_grafic(func, name, func_str, x_arr, y_arr)
    printer(name, cff, e, s, phi, sigma, r2)

    return sigma, func, name, func_str


def to_exp_aprox(x_arr, y_arr):
    cff = np.flip(linear_approx(x_arr, np.log(y_arr)))
    cff[0] = np.e ** cff[0]
    func = lambda x: cff[0] * np.e ** (cff[1] * x)
    func_str = f"{round(cff[0], 4)} * e^({round(cff[1], 4)} * x)"
    name = "Экспоненциальная функция"

    e = count_e(func, x_arr, y_arr)
    s = count_s(e)
    phi = count_phi(func, x_arr)
    sigma = count_sigma(s, len(x_arr))
    r2 = count_r_2(y_arr, phi)

    # util.make_grafic(func, name, func_str, x_arr, y_arr)
    printer(name, cff, e, s, phi, sigma, r2)

    return sigma, func, name, func_str


def to_log_approx(x_arr, y_arr):
    cff = linear_approx(np.log(x_arr), y_arr)
    func = lambda x: cff[0] * np.log(x) + cff[1]
    func_str = f"{round(cff[0], 4)} * log(x) + {round(cff[1], 4)}"
    name = "Логарифмическая функция"

    e = count_e(func, x_arr, y_arr)
    s = count_s(e)
    phi = count_phi(func, x_arr)
    sigma = count_sigma(s, len(x_arr))
    r2 = count_r_2(y_arr, phi)

    # util.make_grafic(func, name, func_str, x_arr, y_arr)
    printer(name, cff, e, s, phi, sigma, r2)

    return sigma, func, name, func_str


def to_degree_approx(x_arr, y_arr):
    cff = np.flip(linear_approx(np.log(x_arr), np.log(y_arr)))
    cff[0] = np.e ** cff[0]
    func = lambda x: cff[0] * x ** cff[1]
    func_str = f"{round(cff[0], 4)} * x^{round(cff[1], 4)}"
    name = "Степенная функция"

    e = count_e(func, x_arr, y_arr)
    s = count_s(e)
    phi = count_phi(func, x_arr)
    sigma = count_sigma(s, len(x_arr))
    r2 = count_r_2(y_arr, phi)

    # util.make_grafic(func, name, func_str, x_arr, y_arr)
    printer(name, cff, e, s, phi, sigma, r2)

    return sigma, func, name, func_str


def pirson_calc(x_arr, y_arr):
    mid_x = np.mean(x_arr)
    mid_y = np.mean(y_arr)
    sxy = 0
    sxx = 0
    syy = 0
    for i in range(len(x_arr)):
        sxy += (x_arr[i] - mid_x) * (y_arr[i] - mid_y)
        sxx += (x_arr[i] - mid_x) ** 2
        syy += (y_arr[i] - mid_y) ** 2
    return sxy / np.sqrt(sxx * syy)


def count_e(func, x_arr, y_arr):
    temp = []
    for i in range(len(x_arr)):
        temp.append(func(x_arr[i]) - y_arr[i])
    return temp


def count_s(ea):
    e = np.array(ea)
    return np.sum(e**2)


def count_r_2(y_arr, phi):
    mid_phi = np.mean(phi)
    s1 = 0
    s2 = 0
    for i in range(len(y_arr)):
        s1 += (y_arr[i] - phi[i]) ** 2
        s2 += (y_arr[i] - mid_phi) ** 2
    return 1 - (s1 / s2)


def count_phi(func, x_arr):
    temp = []
    for i in range(len(x_arr)):
        temp.append(func(x_arr[i]))
    return temp


def count_sigma(s, n):
    return np.sqrt(s / n)
