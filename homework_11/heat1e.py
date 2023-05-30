#!/usr/bin/python3
#
# 1D heat/diffusion equation

import math
import numpy as np
import matplotlib.pyplot as plt

D, Nx, Nt, L, T = 1.0, 40, 400, 1.0, 0.1

t = np.linspace(0, T, num=Nt+1, dtype=float)
x = np.linspace(0, L, num=Nx+1, dtype=float)
dx = x[1] - x[0]
dt = t[1] - t[0]
r = D*dt / (dx*dx)
print ( "r = {}".format(r) )
assert r < 0.5

u = np.empty( (Nx+1,Nt+1), dtype=float )  # macierz na wszystkie wyniki

# initial condition, t=0
u[:,0] = 0.0   # cold rod

#Eksperyment, który wymyśliłem polega na sytuacji, gdy w hucie ktoś nagle chwycił zimny pręt goracymi obcęgami
#za jego dwa końce. Inicjalizuję zimny pręt w t=0. Potem zakładam, że ktoś zaciska obcęgi coraz mocniej, aż
#do wartosci maksymalnej i potem luzuje uścisk. Modeluję to zadając dla obu końców temperaturę przez funkcję
#gaussa (od t) unormowaną do 1. Mam kontrolę nad szybkością zaciskania i luzowania obcęg zmieniając szerokość 
#połówkową funckji. Mała szerokość -> koś szybko chwycił i puszczał pręt. Duża szerokość -> ktoś długo trzymał
#i powoli puszczał pręt. Funkcja scentrowana jest w połowie badanego odcinku czasowego 0.1/2 = 0.05. Mozna to
#traktowac jako impuls temperatury z dwóch stron. Dołączyłem obrazki z różną wartością half_width od 0.1
#pręt trzymany cały badany okres czasu z przynajmniej połowa siły, do 0.001 -> szybki wysoki impuls temperatury
#(pole zawsze jest 1 więc przy szybkim zaciskaniu większa temperatura)

half_width = 0.02 #0.1, 0.05, 0.02, 0.01, 0.001
sigma = half_width / np.sqrt(2 * np.log(2))

# boundary condition,
for j in range(Nt):
    u[Nx,j] = u[0,j] = np.exp(-0.5 * (((j*dt) - 0.05) / sigma) ** 2) / (sigma * np.sqrt(2 * np.pi)) 

# iteration/solution the linear algebraic equations
for j in range(Nt):
    u[1:-1,j+1] = r*u[:-2,j] + (1-2*r)*u[1:-1,j] + r*u[2:,j]

# visualization
print ( u )
plt.title("1D heat equation")
plt.xlabel("time") # odwrotnie!
plt.ylabel("x")

plt.imshow(u, cmap='hot', interpolation='nearest')

plt.colorbar()
plt.show()

# EOF
