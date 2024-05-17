import internal
import numpy as np
import util
import reader

funcs = [
    {"name": "sin(x)", "func": lambda x: np.sin(x)},
    {"name": "cos(x)", "func": lambda x: np.cos(x)},
]

if __name__ == "__main__":
    points = reader.do(funcs)

    internal.finite_differences(points)

    arg = float(input("Введите аргумент: "))

    points_x, points_y = [points[i] for i in range(0, len(points), 2)], [
        points[i] for i in range(1, len(points), 2)
    ]

    res = internal.interpolate_lagrange(points_x, points_y, arg)
    print("Вычисленное значение (Лагранжа):", res)

    util.make_grafic(
        points_x, points_y, internal.interpolate_lagrange, [arg, res], isBlock=False
    )
    h = points_x[1] - points_x[0]
    if not (internal.check_equals(points_x, h)):
        print("Не равностоящие узлы")

        res = internal.interpolate_newton_sep_diff(points_x, points_y, arg)
        print("Вычисленное значение: (Ньютона для разделеннных разностей)", res)

        util.make_grafic(
            points_x, points_y, internal.interpolate_newton_sep_diff, [arg, res]
        )
    else:
        res, func = internal.interpolate_newton_equal_diff(points_x, points_y, arg)
        print("Вычисленное значение: (Ньютона для конечных разностей)", res)

        util.make_grafic(
            points_x, points_y, func, [arg, res]
        )
