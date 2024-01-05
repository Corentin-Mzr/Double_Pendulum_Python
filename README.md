# <center>Double pendulum simulation in Python

### Description
This project aims to simulate a double pendulum in Python.

The following equations describe the physics behind the double pendulum:

$$\ddot{\theta}_1 = -\frac{g}{l_1} \sin(\theta_1) - 
\frac{m_2}{m_1 + m_2} \left(\frac{l_2}{l_1}\right) \ddot{\theta}_2 \sin(\theta_1 - \theta_2)$$

$$\ddot{\theta}_2 = -\frac{g}{l_2} \sin(\theta_2) + 
\frac{m_1}{m_1 + m_2} \left(\frac{l_1}{l_2}\right) \ddot{\theta}_1 \sin(\theta_1 - \theta_2)$$

We do not consider friction.

### Contents
This project is divided in four files:
- Parameters.py contains the parameters of the simulation, 
i.e. characteristics of the pendulum, time span and precision
- Solver.py contains the solver, I use *solve_ivp* from SciPy library
- Animation.py allows to display the pendulum and save the animation, I use Matplotlib to plot the animation
- Main.py calls the previous files

The animation is saved in the *output* directory.