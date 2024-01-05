import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from parameters import l1, l2

matplotlib.rcParams['animation.ffmpeg_path'] = r'C:\ffmpeg\bin\ffmpeg.exe'

matplotlib.use("TkAgg")
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.grid()
text = ax.text(0.05, 0.88, '', transform=ax.transAxes)
line, = ax.plot([], [], "-o", c="blue", lw=2)


def init():
    """ Initialize graph """
    ax.set_xlim(- l1 - l2, l1 + l2)
    ax.set_ylim(- l1 - l2, l1 + l2)
    return line,


def update(i: int,
           x1: list[float] | np.ndarray,
           y1: list[float] | np.ndarray,
           x2: list[float] | np.ndarray,
           y2: list[float] | np.ndarray,
           t0: float,
           tf: float,
           n: int):
    """ 
    Update graph 
    :param i: Current frame
    :param x1: Angle for pendulum 1
    :param y1: Velocity for pendulum 1
    :param x2: Angle for pendulum 2
    :param y2: Velocity for pendulum 2
    :param t0: Initial time
    :param tf: Final time
    :param n: Precision
    """
    x = [0, x1[i], x2[i]]
    y = [0, y1[i], y2[i]]
    line.set_data(x, y)
    text.set_text(f"t = {(i / n) * (tf - t0):.2f}s")
    return line, text,


def display_animation(x1: list[float] | np.ndarray,
                      y1: list[float] | np.ndarray,
                      x2: list[float] | np.ndarray,
                      y2: list[float] | np.ndarray,
                      t0: float,
                      tf: float,
                      n: int,
                      save_file: str):
    """
    Display animation of double pendulum
    :param x1: Angle for pendulum 1
    :param y1: Velocity for pendulum 1
    :param x2: Angle for pendulum 2
    :param y2: Velocity for pendulum 2
    :param t0: Initial time
    :param tf: Final time
    :param n: Precision
    :param save_file: Name of the file
    """
    interval = 1000 * (tf - t0) / n
    ani = FuncAnimation(fig=fig,
                        func=update,
                        frames=n,
                        interval=interval,
                        init_func=init,
                        blit=True,
                        fargs=(x1, y1, x2, y2, t0, tf, n))
    print('Saving animation...')
    ani.save(save_file, writer='ffmpeg', fps=int(n / (tf - t0)))
    print(f'Animation saved at {save_file}')
    plt.tight_layout()
    plt.show()
    return ani
