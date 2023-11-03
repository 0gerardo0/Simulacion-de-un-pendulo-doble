import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Definición de parámetros
g = 9.81  # aceleración debida a la gravedad
m = 1.0   # por definir, masa
d = 1.0   # por definir, distancia

# Ecuación para omega (frecuencia angular)
def omega(m, d, theta):
    return np.sqrt((2*g)/(m*d) * np.sin(theta/2))

# Ecuación para la posición en función del tiempo
def posicion(t, m, d, theta):
    w = omega(m, d, theta)
    return np.sin(w*t)

theta = np.pi / 4  # ángulo inicial
t = np.linspace(0, 10, 1000)  # tiempo

# Preparar la figura y el eje
fig, ax = plt.subplots()
xdata, ydata = [0], [0]
ln, = plt.plot([], [], 'r-')

def init():
    ax.set_xlim(0, 10)
    ax.set_ylim(-1.5, 1.5)
    return ln,

def update(frame):
    xdata.append(t[frame])
    ydata.append(posicion(t[frame], m, d, theta))
    ln.set_data(xdata, ydata)
    return ln,

ani = FuncAnimation(fig, update, frames=range(len(t)), init_func=init, blit=True)

plt.xlabel('Tiempo (s)')
plt.ylabel('Posición (m)')
plt.title('Animación de movimiento oscilatorio')
plt.grid(True)
plt.show()
