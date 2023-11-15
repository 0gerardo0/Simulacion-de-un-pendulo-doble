# Programa de Simulación de Péndulo Doble
## Descripción General
Este programa en Python simula el movimiento de un péndulo doble utilizando las ecuaciones del lagrangiano. Calcula la trayectoria de cada masa del péndulo a lo largo del tiempo, visualiza su movimiento y verifica la conservación de la energía en el sistema.

## Instalación
Se requieren algunas bibliotecas externas que se pueden instalar a través de pip:

```pip install -r modulos_requeridos.txt```

## Cómo Usar
Ejecute el programa con Python. Los parámetros de la simulación se pueden ajustar según sea necesario.

```cd ~/program_pendulo ``` && ```python mov_anim_modif.py```

## Parámetros Modificables
```L1, L2```: Longitudes de los brazos del primer y segundo péndulo.

```m1, m2```: Masas del primer y segundo péndulo.

```y0```: Condiciones iniciales del array, [theta1, theta1_puntito, theta2, theta2_puntito].

```tmax```: Tiempo total de simulación.

```dt```: Paso de tiempo para la simulación.

```error_tolerancia```: Tolerancia de error de la conservacion de la energia.

## Métodos
```energia_del_sistema(y)```: Calcula la energía total del sistema.

```ecua_mov(y, t, L1, L2, m1, m2)```: Define las ecuaciones de movimiento utilizando las ecuaciones de Lagrange.

```trayectoria(i)```: Genera un fotograma para la animación en el paso de tiempo.

```odeint```: Función de la libreria de Scipy para la solucion numerica de ED.


## Notas
--> Ah mas se baja el ```dt``` es mejor el calculo, pero eso indica que tomara mas tiempo computacional, se generaran mas imagenes dependiendo el ```tmax``` y el ```dt```.

--> Para que el script genere las imagenes mas rapido se pueden comentar las impresiones del error y el numero de frame guardado.
```46  print(f"Tiempo {t[i]:.2f} s, Energía Total: {energia:.6f} J, Error de Energía: {error_energia:.2f} J, Suma Acumulada: {acumulado_errores[-1]:.2f} J")```
```90  print(i // frame, '/', t.size // frame)```

--> Descomente ```#from scipy.integrate import solve_ivp``` y ```#sol = solve_ivp(...)``` para usar el método Dormand-Prince. Intercambiar ```ecua_mov(t, y, L1, L2, m1, m2)```. La verdad no es muy bueno este metodo, no aproxima bien la solucion, hay un error bastante grande.

--> Por lo general el error acumulado exedente aparece cuando la solucion numerica por medio de diferentes metodos que se aplican a ```y[ecua_mov]``` no son muy buenos. Solo verifica si es que se mantiene constante en el tiempo. No generara los fotogramas si es que no es bastante confiable la solucion numerica.

--> Se monitorea la conservación de la energía, y el programa se cerrará si excede una tolerancia especificada.