import input as i
import internal
import util


def run():
    reader = i.reader()
    choice = input(
        "Введите 'y', чтобы ввести матрицу из файла, 'n', чтобы ввести вручную: "
    )
    try:
        if choice.lower() == "y":
            filename = input("Введите имя файла: ")
            matrix, accuracy = reader.read_from_file(filename)

        elif choice.lower() == "n":
            matrix, accuracy = reader.read_from_console()
        else:
            raise ValueError("Некорректный выбор.")

    except Exception as e:
        print(f"{e}")
        exit()

    print("Матрица:")
    util.print_table(matrix)
    print("Точность:", accuracy)

    A = matrix[:, :-1]

    try:
        A = internal.sort_diagonal_predominance(matrix[:, :-1])
        print("Матрица с диагональным преобладанием")
        util.print_table(A)
    except ValueError as e:
        print(f"{e}")


    C, D = internal.make_C_and_D_matrix(A, matrix[:, -1:])

    print("Матрица С:")
    util.print_table(C)
    print("Вектор D:")
    util.print_table(D)
    # print(f"Норма матрицы C: {internal.norma(C)} < 1 = {internal.check_norma(C)}")
    print(f"Норма матрицы C: {internal.norma_all(C)} < 1 = {internal.check_norma(C)}")

    res, headers = internal.iterational_method(C, D, accuracy, 20)

    print("Таблица:")
    util.print_table(res, headers)


if __name__ == "__main__":
    run()
