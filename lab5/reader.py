import sys
import numpy as np


def console():
    try:
        return list(
            map(
                lambda x: float(x.strip()),
                [i for i in input("Ведите точки через пробел: ").split(" ") if i != ""],
            )
        )
    except:
        raise ValueError("Введите точки в правильном формате")


def file():

    try:
        filename = sys.argv[1]
    except:
        filename = input("Напишите имя файла: ").strip()

    try:
        with open(filename, "r") as file:
            return list(map(float, file.read().strip().split()))
    except FileNotFoundError:
        raise ValueError("Файл не был найден")
    except:
        print("Произошла ошибка при чтении файла")
        exit()


def func(funcs):
    try:
        in_str = [f"{i}. {val['name']}" for (i, val) in enumerate(funcs)]
        print(*in_str, sep="\n")
        func = funcs[int(input("Ввод: ").strip())]["func"]

        a, b = map(
            lambda x: float(x.strip()),
            input("Введите интервал через пробел (a, b): ").split(" "),
        )
        count = int(input("Введите кол-во точек: ").strip())
        points = np.linspace(a, b, count)

        data = []
        for i in points:
            data.append(i)
            data.append(func(i))

        return data
    except:
        raise ValueError("Вы ввели не правильный индекс функции")


def do(funcs):
    variant = input("1. Вручную\n2. Из файла\n3. На основе функции\nВвод: ")
    data = None
    try:
        match variant.strip():
            case "1":
                data = console()
            case "2":
                data = file()
            case "3":
                data = func(funcs)
    except Exception as e:
        print(e.args[0])
        exit()

    return data
