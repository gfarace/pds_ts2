#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 30/8/2021

@author: Gisela Farace

Descripción: Tarea semanal 2
Desarrollar un algoritmo que calcule la transformada discreta de Fourier (DFT)
------------
"""

# Importación de módulos para Jupyter

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pdsmodulos as pds

#%% Funciones

# Senoidal

def senoidal(vmax, dc, ff, ph, nn, fs):
    ts = 1/fs # tiempo de muestreo
    df = fs/nn # resolución espectral 
    
    # grilla de sampleo temporal
    tt = np.linspace(0, (nn-1)*ts, nn).flatten()
    
    # grilla de sampleo frecuencial
    sen = vmax*np.sin(2*np.pi*ff*tt + ph)+dc
    
    return tt, sen

# La DFT se define como:
# X_k = sumatoria{x_n.e^(-j2.pi.k.n/N)} desde N=0 a N-1

def dft(xx):
    N = xx.size
    n = np.arange(N)    
    k = n.reshape((N, 1)) 
    XX = np.zeros(N,dtype=np.int8) # Matriz de Nx1 ceros

    exponencial = np.exp(-2j*np.pi*k*n/N)
    
    XX = np.dot(exponencial, xx) #Producto de dos arrays

    return  XX 
#%% Senoidal
# Parámetros
vmax = 1
dc = 0
ff = 1
ph = 0
nn = 1000
fs = 100 

tt,xx = senoidal(vmax, dc, ff, ph, nn, fs)

plt.figure(1)
line_hdls = plt.plot(tt, xx)
plt.title('Señal senoidal')
plt.xlabel('tiempo [seg]')
plt.ylabel('Amplitud [V]')

axes_hdl = plt.gca()

plt.show()

#%% DFT senoidal
XX = dft(xx)

# Grilla de frecuencia
N = XX.size
n = np.arange(N)
ff = fs*n/N 

plt.figure(2)
line_hdls = plt.plot(ff, abs(XX))
plt.title('Transformada de Fourier')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Amplitud')

axes_hdl = plt.gca()

plt.show()

#%% Usando la DFT rápida FFT

fourier = np.fft.fft(xx)
freq = np.fft.fftfreq(fourier.size,d=1/fs)*fs

plt.figure(3)
line_hdls = plt.plot(freq, abs(fourier))
plt.title('Transformada de Fourier rápida (FFT)')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Amplitud')
axes_hdl = plt.gca()

plt.show()

#%% Ruido con varianza 4
var = 4
ruido = var*np.random.random_sample(N)

plt.figure(4)
line_hdls = plt.plot(np.arange(ruido.size),ruido)
plt.title('Señal senoidal')
plt.xlabel('tiempo [seg]')
plt.ylabel('Amplitud [V]')

axes_hdl = plt.gca()

plt.show()

t_ruido = np.fft.fft(ruido)
freq_ruido = np.fft.fftfreq(t_ruido.size)

plt.figure(5)
line_hdls = plt.plot(freq_ruido, abs(t_ruido))
plt.title('Transformada de Fourier ruido')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Amplitud')

plt.show()




