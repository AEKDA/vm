import sympy as sp
import numpy as np
import re


def math_funcs(funcs: list[str]):

    print("Введите номер уравнения")
    for index, fun in enumerate(funcs):
        print(f"{index+1}. {fun}")
    ans = input("Ввод: ")

    try:
        if ans.isdigit():
            expression = funcs[int(ans) - 1]
        else:
            raise ValueError("Неверный ввод.")
        exp = expression.split(";")
        expression = exp[0].split(",")
        expression_phi = exp[1].split(",")
        if len(expression) == 1:
            expression = expression[0]
            f = sp.sympify(expression)
        else:
            f = [sp.sympify(exp) for exp in expression]
            f_phi = [sp.sympify(exp) for exp in expression_phi]

        print("Исходная функция:", f)
        return f, f_phi
    except:
        raise ValueError("Неверный ввод.")


def math_func(funcs: list[str]):

    print("Введите номер уравнения")
    for index, fun in enumerate(funcs):
        print(f"{index+1}. {fun}")
    ans = input("Ввод: ")

    try:
        if ans.isdigit():
            expression = funcs[int(ans) - 1]
        else:
            raise ValueError("Неверный ввод.")
        expression = expression.split(",")
        if len(expression) == 1:
            expression = expression[0]
            f = sp.sympify(expression)
        else:
            f = [sp.sympify(exp) for exp in expression]

        print("Исходная функция:", f)
        return f
    except:
        raise ValueError("Неверный ввод.")


def method(methods):

    print("Введите номер метода: ")
    for index, method in enumerate(methods):
        print(f"{index+1}. {method['name']}")

    ans = input("Ввод: ")

    if not ans.isdigit() or int(ans) - 1 not in [
        index for index, _ in (enumerate(methods))
    ]:
        raise ValueError("Неверный ввод. Метода с указаным номером не существует")
    return methods[int(ans) - 1]
