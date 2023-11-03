close all
clear all
clc

t = linspace(0, pi/4, 10000);  % Valores de tiempo

R = 4;
L = 10e-3;
C = 100e-6;

w = 60;
Vo = 120;

wo = 1/sqrt(L*C);
beta = R/(2*L);

A = (Vo*w/L)*(1/sqrt((wo^2 - w^2)^2 + 4*beta^2 *w^2));

phi = atan((2*w*beta)/(wo^2 - w^2));

ip = A*cos(w*t-phi);

ic = Vo*exp(-beta-t).*(cos(t*sqrt(wo^2 - beta^2)));

i = ic + ip;

w = linspace(0,2000,10000);

D = 1./sqrt((wo^2 - w.^2).^2 + 4*beta^2*w.^2);

figure 1
plot(w,D)
#plot(t, ip);  % Graficar x en función de y
#hold on
#plot(t,ic);
#hold on
#plot(t,i)

xlabel('Eje X');  % Etiqueta del eje X
ylabel('Eje Y');  % Etiqueta del eje Y
title('Gráfico de Datos');  % Título del gráfico
legend('Datos');  % Leyenda de la serie de datos

grid on;  % Mostrar cuadrícula en el gráfico

