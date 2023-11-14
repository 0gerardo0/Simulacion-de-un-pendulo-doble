import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.animation import FuncAnimation

l1=1
l2=2
m1=1
m2=1
g=9.81
def movimiento(y, t, l1, l2, m1, m2):
    theta1, theta1_p, theta2, theta2_p = y
    O,P = np.cos(theta1-theta2), np.sin(theta1-theta2)
    th1_p = theta1_p
    th1_dp = (m2*g*np.sin(theta2)*O - m2*P*(l1*theta1_p**2*O + l2*theta2_p**2) - (m1+m2)*g*np.sin(theta1)) / l1 / (m1 + m2*P**2)
    th2_p = theta2_p
    th2_dp = ((m1+m2)*(l1*theta1_p**2*P - g*np.sin(theta2) + g*np.sin(theta1)*O) +  m2*l2*theta2_p**2*P*O) / l2 / (m1 + m2*P**2)
    return th1_p, th1_dp, th2_p, th2_dp
y0 = np.array([3*np.pi/7, 0, np.pi/2, 0])
tmax, dt = 20, 0.04 
t=np.arange(0, tmax, dt)
y = odeint(movimiento, y0, t, args=(l1, l2, m1, m2))
theta1, theta2 = y[:,0], y[:,2]
x1 = l1 * np.sin(theta1)
y1 = -l1 * np.cos(theta1)
x2 = x1 + l2 * np.sin(theta2)
y2 = y1 - l2 * np.cos(theta2)
print("Longitud de x1 {}, x2 {}, y1 {}, y2 {}." .format(len(x1), len(x2), len(y1), len(y2)))
seg_trayectoria = 1
max_trayectoria = int(seg_trayectoria / dt)
r = 0.03 
fig, ax = plt.subplots(figsize=(6,6))
def init():
    ax.clear()
    ax.set_xlim(-l1 - 1, l1 + 1)
    ax.set_ylim(-l1 - 1, l1 + 1)
    return []
def animate(i):
    ax.clear()
    ax.plot(0, 0, marker='s', markersize=10, color='red')
    x1_i, y1_i, x2_i, y2_i = x1[i], y1[i], x2[i], y2[i]
    ax.plot([0, x1_i, x2_i], [0, y1_i, y2_i], color='black', lw=2.5, marker='o', markersize=8, markerfacecolor='blue', markeredgecolor='black')
    ax.add_patch(Circle((x1_i, y1_i), r, color='blue'))
    ax.add_patch(Circle((x2_i, y2_i), r, color='pink'))
    if i >= max_trayectoria:
        ax.plot(x1[i - max_trayectoria:i], y1[i - max_trayectoria:i], 'g-', lw=1, alpha=0.5)
        ax.plot(x2[i - max_trayectoria:i], y2[i - max_trayectoria:i], 'r-', lw=1, alpha=0.5)
    nuevo_limite_x = 3
    nuevo_limite_y = 3 
    ax.set_xlim(-nuevo_limite_x, nuevo_limite_x)
    ax.set_ylim(-nuevo_limite_y, nuevo_limite_y)
    return []
ani = FuncAnimation(fig, animate, frames=len(t), init_func=init, blit=True, repeat=False, interval=5)
plt.show()