import numpy as np
import methods
import internal
import reader
from tabulate import tabulate
import util


funcs = [
    {
        "str": "y' = y + (1 + x) * y^2",
        "f": lambda x, y: y + (1 + x) * y**2,
    },
    {
        "str": "y' = x^2 * y",
        "f": lambda x, y: x**2 * y,
    },
    {
        "str": "y' = 3 * x ** 2 * y + x^2 * exp(x^3)",
        "f": lambda x, y: 3 * x**2 * y + x**2 * np.exp(x**3),
    },
]


if __name__ == "__main__":
    try:
        func = reader.DE(funcs)

        x1, x2 = map(
            lambda x: float(x.strip()),
            input("Введите интервал дифференцирования a b через пробел: ").split(" "),
        )
        y0 = float(input(f"Введите y({x1}): "))
        h = float(input(f"Введите шаг h: "))
        eps = float(input(f"Введите точноесть eps: "))
    except:
        print("Не корректный ввод")
        exit(-1)
    euler, h1 = internal.one_step(func, methods.euler, x1, x2, y0, h, eps, 1)

    upgraded_euler, h2 = internal.one_step(
        func, methods.upgraded_euler, x1, x2, y0, h, eps, 2
    )
    adams, real, h3 = internal.multistep(func, methods.adams, x1, x2, y0, h, eps)

    print(
        "Метод Эйлера",
        tabulate(map(lambda x: (x[0], x[1]), euler), headers=["X", "Y"]),
        sep="\n",
    )
    print("Усов метод Эйлера", tabulate(upgraded_euler, headers=["X", "Y"]), sep="\n")

    print(
        "Метод Адамса",
        tabulate(
            list(
                map(
                    lambda x: [x[0][0], x[0][1], x[1]],
                    list(zip(adams, real)),
                )
            ),
            headers=["X", "Y", "Реальное значение Y"],
        ),
        sep="\n",
    )
    print(f"Итоговый шаг для метода эйлера {h1}")
    print(f"Итоговый шаг для модернизированного метода эйлера {h2}")
    print(f"Итоговый шаг для метода Адамса {h3}")

    util.plot(real, euler, upgraded_euler, adams)
