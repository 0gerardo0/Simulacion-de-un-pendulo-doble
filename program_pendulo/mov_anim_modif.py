import os
import sys
import numpy as np
from scipy.integrate import odeint
#from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
directory = "trayectoria"

# Longitudes, masas y gravedad
L1, L2, m1, m2, g = 5, 2.5, 1, 1, 9.81
# Funcion de energia total del sistemna: Ecuaciones de energia cinetica y potencial
def energia_del_sistema(y):
    th1, th1_puntito, th2, th2_puntito = y.T #funcion y de variables de inicializacion
    V = -(m1+m2)*L1*g*np.cos(th1) - m2*L2*g*np.cos(th2)
    T = 0.5*m1*(L1*th1_puntito)**2 + 0.5*m2*((L1*th1_puntito)**2 + (L2*th2_puntito)**2 +
            2*L1*L2*th1_puntito*th2_puntito*np.cos(th1-th2))
    return T + V
# Ecuaciones de movimiento, soluciones de las ecuaciones de lagrange
def ecua_mov(y, t, L1, L2, m1, m2):
    theta1, theta1_p, theta2, theta2_p = y

    theta1_puntito = theta1_p
    theta1_dopuntos = (m2*g*np.sin(theta2)*np.cos(theta1-theta2) - m2*np.sin(theta1-theta2)*(L1*theta1_p**2*np.cos(theta1-theta2) + L2*theta2_p**2) - (m1+m2)*g*np.sin(theta1)) / L1 / (m1 + m2*np.sin(theta1-theta2)**2)
    theta2_puntito = theta2_p
    theta2_dopuntos = ((m1+m2)*(L1*theta1_p**2*np.sin(theta1-theta2) - g*np.sin(theta2) + g*np.sin(theta1)*np.cos(theta1-theta2)) +  m2*L2*theta2_p**2*np.sin(theta1-theta2)*np.cos(theta1-theta2)) / L2 / (m1 + m2*np.sin(theta1-theta2)**2)
    return theta1_puntito, theta1_dopuntos, theta2_puntito, theta2_dopuntos

# Parametros de inicializacion: theta1, theta1_p, theta2, theta2_p 
y0 = np.array([3*np.pi/4, 0, np.pi/2, 0])

# Solucion numerica por el metodo de Método de Dormand-Prince de orden 8(5,3) [Para utilizar otro solo de cambia method]
# Solucion numerica scipy
tmax, dt = 30, 0.01 #Tiempo de simulacion y diferencial de pasos
t=np.arange(0, tmax+dt, dt)
y = odeint(ecua_mov, y0, t, args=(L1, L2, m1, m2))
#sol = solve_ivp(ecua_mov, [0, tmax], y0, args=(L1, L2, m1, m2), method='DOP853', t=np.arange(0, tmax+dt, dt))


# Monitoreo de la energia del sistema, si es que se conserva en el tiempo
energia_total = energia_del_sistema(y)
energia_inicial = energia_del_sistema(y0)
acumulado_errores = []
for i, energia in enumerate(energia_total):
    error_energia = np.max(np.sum(np.abs(energia - energia_inicial)))
    acumulado_errores = [error_energia] if i == 0 else acumulado_errores + [acumulado_errores[-1] + error_energia]
    print(f"Tiempo {t[i]:.2f} s, Energía Total: {energia:.6f} J, Error de Energía: {error_energia:.2f} J, Suma Acumulada: {acumulado_errores[-1]:.2f} J")
error_tolerancia = 0.5
if np.max(np.sum(np.abs(energia_total - energia_inicial))) > error_tolerancia:
    sys.exit('No conserva la energia, excede la tolerancia {}.'.format(error_tolerancia))

# Coordenadas cartesianas de m1 y m2
theta1, theta2 = y[:,0], y[:,2] # Extraccion de las posiciones angulares de las masas
x1 = L1 * np.sin(theta1)
y1 = -L1 * np.cos(theta1)
x2 = x1 + L2 * np.sin(theta2)
y2 = y1 - L2 * np.cos(theta2)

# Parametros de dibujo en la animacion
r = 0.5 #Radio de las masas
seg_trayectoria = 1 
max_trayectoria = int(seg_trayectoria / dt) #Puntos de impresion de la trajectoria
if not os.path.exists(directory):
    os.makedirs(directory)
def trayectoria(i):
    if i < len(x1):
        ax.plot([0, x1[i], x2[i]], [0, y1[i], y2[i]], lw=3, c='k') # Dibujo de los brazos de la del pendulo  --lw[grosor] --c[color]
    c0 = Circle((0, 0), r/2, fc='k', zorder=10) # Dibujo del punto de anclaje
    c1 = Circle((x1[i], y1[i]), r, fc='b', ec='b', zorder=10) # Dibujo de la masa 1 --fc[color] --ec[fc-contorno]
    c2 = Circle((x2[i], y2[i]), r, fc='r', ec='r', zorder=10) # Dibujo de la masa 2 --fc[color] --ec[fc-contorno]
    # Dibujan la imagen
    ax.add_patch(c0)
    ax.add_patch(c1)
    ax.add_patch(c2)

    # Centra la imagen en el punto de anclaje fijo, y asegura que los ejes sean iguales
    ax.set_xlim(-L1-L2-r, L1+L2+r)
    ax.set_ylim(-L1-L2-r, L1+L2+r)
    ax.set_aspect('equal', adjustable='box')
    plt.axis('off')
    plt.savefig('trayectoria/img_frame{:04d}.png'.format(i//frame), dpi=97)
    plt.cla()

# Generacion de imagenes de en una taza de 10 fps
fps = 10
frame = int(1/fps/dt)
fig = plt.figure(figsize=(9, 9), dpi=92)
ax = fig.add_subplot(111)

for i in range(0, t.size, frame):
    print(i // frame, '/', t.size // frame)
    trayectoria(i)