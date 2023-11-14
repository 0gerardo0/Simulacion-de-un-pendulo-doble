# Programa de Simulación de Péndulo Doble
## Descripción General
Este programa en Python simula el movimiento de un péndulo doble utilizando las leyes de la física. Calcula la trayectoria de cada masa del péndulo a lo largo del tiempo, visualiza su movimiento y verifica la conservación de la energía en el sistema.

## Instalación
Se requieren algunas bibliotecas externas que se pueden instalar a través de pip:

```pip install -r requirements.txt```

## Cómo Usar
Ejecute el programa con Python. Los parámetros de la simulación se pueden ajustar según sea necesario.

```cd ~/program_pendulo && python mov_anim_modif.py```

## Parámetros Modificables
```*__L1, L2__*```: Longitudes de los brazos del primer y segundo péndulo.

```*__m1, m2__*```: Masas de las masas del primer y segundo péndulo.

```*__y0__*```: Condiciones iniciales del array, [theta1, theta1_puntito, theta2, theta2_puntito].

```*__tmax__*```: Tiempo total de simulación.

```*__dt__*```: Paso de tiempo para la simulación.

## Métodos
```*__energia_del_sistema(y)__*```: Calcula la energía total del sistema.

```*__ecua_mov(y, t, L1, L2, m1, m2)__*```: Define las ecuaciones de movimiento utilizando las ecuaciones de Lagrange.

```*__trayectoria(i)__*```: Genera un fotograma para la animación en el paso de tiempo.


## Notas
--> Descomente ```#from scipy.integrate import solve_ivp``` y ```#sol = solve_ivp(...)``` para usar el método Dormand-Prince. Intercambiar ```*__ecua_mov(t, y, L1, L2, m1, m2)__*```

--> Se monitorea la conservación de la energía, y el programa se cerrará si excede una tolerancia especificada.