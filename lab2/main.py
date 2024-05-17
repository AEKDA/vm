import util
import input as reader
import newton
import half_div
import iter
import system_iter
import sympy as sp

funcs = [
    "2*x**3 + 3.41*x**2 - 23.74*x + 2.95",
    "-1.8*x^3 - 2.94*x^2+10.37*x +5.38",
    "x^3 - 1.89*x^2 - 2*x + 1.76",
]

funcs_system = [
    "3 + cos(y) - x, 0.5 - cos(x-1) - y; 3 + cos(y), 0.5 - cos(x-1)",
    "x + cos(y - 1) - 0.7, sin(x) + 2*y - 2; 0.7 - cos(y -1), 1 -sin(x)/2",
    "0.1 *x^2 + x + 0.2*y^2 - 0.3, 0.2 * x^2 + y + 0.1 * x * y - 0.7; -0.1 *x^2 - 0.2*y^2 + 0.3, -0.2 * x^2 - 0.1 * x * y + 0.7",
]
methods = [
    {"name": "newton", "f": newton.solve},
    {"name": "half-division", "f": half_div.solve},
    {"name": "iteration", "f": iter.solve},
    {"name": "system-iteration", "f": system_iter.solve},
]


def check(func, a, b):
    x = sp.Symbol("x")
    if func.subs(x, a) * func.subs(x, b) < 0:
        print("Уравнение имеет хотябы один корень")
    else:
        print("Невозможно точно сказать сколько корней")
    return ""


def run():

    method = reader.method(methods)
    if method["name"] == "system-iteration":
        func, func_phi = reader.math_funcs(funcs_system)

        util.make_graphics(func)

        init = list(map(float, input("Ввод начального приближения: ").split(" ")))
    else:
        func = reader.math_func(funcs)
        util.make_graphic(func)
        init = list(map(float, input("Ввод интервала a и b через пробел: ").split(" ")))

        print(check(func, init[0], init[1]))

    eps = float(input("Ввод точности: "))

    match method:
        case {"name": "newton", "f": f}:
            print(f(func, init[0], init[1], eps))

        case {"name": "half-division", "f": f}:
            print(f(func, init[0], init[1], eps))

        case {"name": "iteration", "f": f}:
            print(f(func, init[0], init[1], eps, 1000))

        case {"name": "system-iteration", "f": f}:
            print(f(func, func_phi, init, eps, 100))

        case _:
            raise ValueError("Ошибка!")


if __name__ == "__main__":
    try:
        run()
    except Exception as e:
        print(f"{e}")
