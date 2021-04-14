def f(x):
    return x * x * x - 12 * x - 8

def secant(x0, x1, eps):
    f_x0 = f(x0)
    f_x1 = f(x1)
    iteration_counter = 0
    if f_x0 * f_x1 < 0:
        while abs(f_x1) > eps and iteration_counter < 100:
            try:
                denominator = float(f_x1 - f_x0) / (x1 - x0)
                x = x1 - float(f_x1) / denominator
            except ZeroDivisionError:
                return None
            x0 = x1
            x1 = x
            f_x0 = f_x1
            f_x1 = f(x1)
            iteration_counter += 1
        if abs(f_x1) > eps:
            iteration_counter = -1
        return x
    else:
        return None