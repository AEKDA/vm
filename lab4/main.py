import re
import reader
import numpy as np
import approx
import util


if __name__ == "__main__":

    try:
        points_x, points_y = reader.funcs()

        if not (len(points_x) >= 6 and len(points_x) <= 12):
            raise ValueError
        if not (len(points_y) >= 6 and len(points_y) <= 12):
            raise ValueError
    except:
        print("Вы вели не правильное кол-во чисел")
        exit()

    print(points_x, points_y)

    points_x = np.array(points_x)
    points_y = np.array(points_y)
    x_low = points_x <= 0
    y_low = points_y <= 0

    r = approx.pirson_calc(points_x, points_y)
    print("\n", f"Коэффициент пирсона r: {r}", "\n")

    res = []

    res.append(approx.to_linear(points_x, points_y))
    res.append(approx.to_second_degree(points_x, points_y))
    res.append(approx.to_third_degree(points_x, points_y))
    try:
        if not y_low.any():
            res.append(approx.to_exp_aprox(points_x, points_y))
        else:
            raise ValueError("Экспоненциальная функиця")
        if not x_low.any():
            res.append(approx.to_log_approx(points_x, points_y))
        else:
            raise ValueError("Логорифмическая функция")
        if not x_low.any() and not y_low.any():
            res.append(approx.to_degree_approx(points_x, points_y))
        else:
            raise ValueError("Степенная функция")
    except Exception as e:
        print(f"Нельзя вычислить log от отрицательного значения: {e.args[0]}")

    vals = [i[0] for i in res]

    min_vals = np.where(vals == np.nanmin(vals))[0]

    if len(min_vals) > 1:
        print("\nНесколько лучших апроксимаций:")
    else:
        print("\nЛучшая апроксимация:")
    for m in min_vals:
        print(res[m][2])
        print("Значение среднеквадратичного отклонения:", res[m][0])
        util.make_grafic(res[m][1], res[m][2], res[m][3], points_x, points_y)
