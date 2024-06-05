from scipy.integrate import odeint


def check(ans, ans_new, eps, accuracy):
    for i in range(len(ans)):
        if i * 2 < len(ans_new):
            accur = abs(ans[i][1] - ans_new[i * 2][1]) / (2**accuracy - 1)
            if accur > eps:
                return False
    print(f"точность: {accur}")
    return True


def one_step(func, method, x1, x2, y0, h, eps, accuracy, stepCount=100):
    f = func["f"]
    ans = method(f, x1, x2, y0, h)

    for _ in range(stepCount):
        h_new = h / 2
        ans_new = method(f, x1, x2, y0, h_new)

        if check(ans[1:], ans_new, eps, accuracy):
            break

        h = h_new
        ans = ans_new
    return ans, h


def find_real_val(f, x_arr, y0):
    y = odeint(lambda x, y: f(y, x), y0, x_arr)
    return y


# def multistep(func, method, x1, x2, y0, h, eps):
#     f = func["f"]
#     ans = method(f, x1, x2, y0, h)

#     real_vals = [i[0] for i in find_real_val(f, [i[0] for i in ans], y0)]

#     return ans, real_vals, h


def multistep(func, method, x1, x2, y0, h, eps, stepCount=100):
    f = func["f"]

    for _ in range(stepCount):
        ans = method(f, x1, x2, y0, h)
        real_vals = [i[0] for i in find_real_val(f, [i[0] for i in ans], y0)]
        flag = False
        for i in range(len(real_vals)):
            if abs(real_vals[i] - ans[i][1]) > eps:
                flag = True
                break

        if not flag:
            break

        h /= 2
        
    return ans, real_vals, h
