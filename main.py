from solver import solve
from animation import display_animation
from parameters import t10, v10, t20, v20, t0, tf, n


if __name__ == '__main__':
    # Solve for given initial conditions
    s0 = (t10, v10, t20, v20)
    x1, y1, x2, y2 = solve(s0, t0, tf, n)

    # Display double pendulum
    save_file = r"output/video.mp4"
    display_animation(x1, y1, x2, y2, t0, tf, n, save_file)

