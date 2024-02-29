import numpy as np


class reader:
    def __init__(self) -> None:
        pass

    def read_from_console(self):
        try:
            accuracy = float(input("Введите точность: "))

            rows = int(input("Введите размерность матрицы: "))
            cols = rows + 1

            matrix = np.zeros((rows, cols))
            print(f"Введите элементы матрицы {rows}x{cols}:")
            for i in range(rows):
                row = input().strip().split()
                if len(row) != cols:
                    raise ValueError("Неверное количество элементов в строке.")

                matrix[i] = [float(elem) for elem in row]
        except Exception as e:
            raise ValueError(f"Вы ввели не корректное значение: {e}")
        return matrix, accuracy

    def read_from_file(self, filename):
        try:
            with open(filename, "r") as file:
                accuracy = float(file.readline().strip())
                matrix = np.loadtxt(file)
                return matrix, accuracy

        except FileNotFoundError:
            raise ValueError("Файл не найден.")

        except Exception as e:
            raise Exception("Произошла ошибка при чтении файла:", e)
