import numpy as np


def hermite_curve(event_1, event_2, m0, m1):
    """Вычисляет точку на кривой Эрмита для заданного параметра t.

    Аргументы:
    t -- параметр кривой в диапазоне от 0 до 1.
    p0 -- начальная точка кривой (x0, y0).
    p1 -- конечная точка кривой (x1, y1).
    m0 -- направление касательной в начальной точке (dx0, dy0).
    m1 -- направление касательной в конечной точке (dx1, dy1).

    Возвращает:
    Точку на кривой Эрмита в виде (x, y).
    """

    print(event_1, event_2, m0, m1)
    t_values = np.linspace(0, 1, num=1000)

    points = []

    for t in t_values:
        p0 = (event_1.x, event_1.y)
        p1 = (event_2.x, event_2.y)

        t2 = t * t
        t3 = t2 * t

        h00 = 2 * t3 - 3 * t2 + 1
        h10 = t3 - 2 * t2 + t
        h01 = -2 * t3 + 3 * t2
        h11 = t3 - t2

        x = h00 * p0[0] + h10 * m0[0] + h01 * p1[0] + h11 * m1[0]
        y = h00 * p0[1] + h10 * m0[1] + h01 * p1[1] + h11 * m1[1]

        points.append((x, y, 0))

    return points
