# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 00:02:34 2018

@author: filip
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft

Fs = 8000
T = 1.0/ Fs
T0 = 0.064
N = T0 / T
df = Fs / N

t = np.linspace(0.0,T0-T,N)
x1 = 5*np.cos(2*np.pi*500*t) 
x2 = 10*np.cos(2*np.pi*1000*t) 
x3 = 15*np.cos(2*np.pi*1500*t)

x = x1 + x2 + x3 
plt.figure(1)
plt.plot(x)
plt.legend(['Señal x = x1 + x2 + x3'])
plt.ylabel('Amplitud')
plt.xlabel('Tiempo t')
plt.show;

X= fft(x)
A = np.abs(X)/N
n = np.linspace(0.0,N*df,N)

plt.figure(2)
plt.plot(n,A, 'g')
plt.legend(['Espectro x = x1 + x2 + x3'])
plt.ylabel('Amplitud')
plt.xlabel('Frecuencia Hz')
plt.show;


# Demostración componente en frecuencia de X1
X= fft(x1)
A = np.abs(X)/N
n = np.linspace(0.0,N*df,N)

plt.figure(3)
plt.plot(n,A, 'y')
plt.legend(['Espectro x1 = 5*np.cos(2*np.pi*500*t)'])
plt.ylabel('Amplitud')
plt.xlabel('Frecuencia Hz')
plt.show;

# Demostración componente en frecuencia de X2
X= fft(x2)
A = np.abs(X)/N
n = np.linspace(0.0,N*df,N)

plt.figure(4)
plt.plot(n,A, 'y')
plt.legend(['Espectro x2 = 5*np.cos(2*np.pi*1000*t)'])
plt.ylabel('Amplitud')
plt.xlabel('Frecuencia Hz')
plt.show;

# Demostración componente en frecuencia de X3
X= fft(x3)
A = np.abs(X)/N
n = np.linspace(0.0,N*df,N)

plt.figure(5)
plt.plot(n,A, 'y')
plt.legend(['x3 = 5*np.cos(2*np.pi*1500*t)'])
plt.ylabel('Amplitud')
plt.xlabel('Frecuencia Hz')
plt.show;