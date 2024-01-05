import numpy as np
# Mass in kg
# Length in m
# Angles in rad
# Velocity in rad/s

# Pendulum 1 (length, mass, angle, velocity)
l1: float = 0.5
m1: float = 1
t10: float = 180 * np.pi / 180
v10: float = 0

# Pendulum 2 (length, mass, angle, velocity)
l2: float = 0.25
m2: float = 2
t20: float = 90 * np.pi / 180
v20: float = 0

# Gravity
g: float = 9.81

# Time span and precision
t0: float = 0
tf: float = 30
n: int = 3000
