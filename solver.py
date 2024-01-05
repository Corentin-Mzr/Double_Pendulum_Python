import numpy as np
from scipy.integrate import solve_ivp
from typing import Any
from parameters import l1, l2, m1, m2, g


def ds_dt(t: float, s: tuple) -> list[float]:
    """
    :param t: time
    :param s: vector
    :return: ds/dt
    """
    t1, v1, t2, v2 = s
    cos: float = np.cos(t1 - t2)
    sin: float = np.sin(t1 - t2)
    return [
        v1,
        (
                m2 * g * sin * cos
                - m2 * sin * (l1 * v1 ** 2 * cos + l2 * v2 ** 2)
                - (m1 + m2) * g * np.sin(t1)
        ) / l1 / (m1 + m2 - m2 * cos ** 2),
        v2,
        (
                (m1 + m2) * (l1 * v1 ** 2 * sin - g * np.sin(t2) + g * np.sin(t1) * cos)
                + m2 * l2 * v2 ** 2 * sin * cos
        ) / l2 / (m1 + m2 * sin ** 2)
    ]


def solve(s0: tuple, t0: float, tf: float, n: int) -> tuple:
    """ Solve differential equation for given initial conditions, on given time span """
    print('Solving...')
    t: np.ndarray[float] = np.linspace(t0, tf, n)
    sol: Any = solve_ivp(fun=ds_dt, t_span=(t0, tf), y0=s0, method="DOP853", t_eval=t, rtol=1e-13, atol=1e-13)

    th1: list[float] = sol.y[0]
    th2: list[float] = sol.y[2]

    x1: np.ndarray[float] = l1 * np.sin(th1)
    y1: np.ndarray[float] = - l1 * np.cos(th1)
    x2: np.ndarray[float] = x1 + l2 * np.sin(th2)
    y2: np.ndarray[float] = y1 - l2 * np.cos(th2)
    print('Ended solving')

    return x1, y1, x2, y2
