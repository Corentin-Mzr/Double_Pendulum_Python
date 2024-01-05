import matplotlib
import matplotlib.animation
import numpy as np
from solver import solve
from animation import display_animation

matplotlib.rcParams['animation.ffmpeg_path'] = r'C:\ffmpeg\bin\ffmpeg.exe'

if __name__ == '__main__':
    # Initial angle and velocity for pendulum 1
    t10 = 180 * np.pi / 180
    v10 = 0

    # Initial angle and velocity for pendulum 2
    t20 = 90 * np.pi / 180
    v20 = 0

    # Time span and precision
    t0 = 0
    tf = 30
    n = 3000

    # Solve for given initial conditions
    s0 = (t10, v10, t20, v20)
    x1, y1, x2, y2 = solve(s0, t0, tf, n)

    # Display double pendulum
    save_file = r"output/video.mp4"
    display_animation(x1, y1, x2, y2, t0, tf, n, save_file)

