import sys


def funcs() -> list:
    try:
        filename = sys.argv[1]
        try:
            with open(filename, "r") as file:
                points = list(map(float, file.read().strip().split()))
        except FileNotFoundError:
            raise ValueError("Файл не был найден")
        except Exception as e:
            print(e)
            exit()

    except:
        points = list(
            map(
                lambda x: float(x.strip()),
                [
                    i
                    for i in input("Ведите 8-12 точек через пробел: ").split(" ")
                    if i != ""
                ],
            )
        )

    points_x, points_y = [points[i] for i in range(0, len(points), 2)], [
        points[i] for i in range(1, len(points), 2)
    ]
    return points_x, points_y
