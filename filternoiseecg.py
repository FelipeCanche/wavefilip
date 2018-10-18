# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 20:56:04 2018

@author: filip
"""
import pandas as pd # Libreria para importar archivos
#import numpy as np
import matplotlib.pyplot as plt
import pywt
#import scipy.interpolate as interpld


file2 = "ECGRESP.xlsx"
dff = pd.read_excel(file2, sheet_name = 'Hoja1')

x = dff['Datos']
y = dff['Muestras']

#print(x)
#print(y)

#plt.plot(y,x)
#plt.ylabel('Muestras')
#plt.xlabel('N')
#plt.show



plt.figure(1,figsize=(20,12))
plt.plot(y,x,'g')
plt.legend(['Original signal'])
plt.ylabel('Muestras')
plt.xlabel('N')
plt.show;

# The descomposition Symmlet 5 with a total of 5 levels:
w = pywt.Wavelet('sym5')
coeffs = pywt.wavedec(x,w,level=5)

#  Reconstruction of the signal 


recon5 = pywt.waverec(coeffs[:-5] + [None] * 5, w) 

recons = x-recon5[0:1500]
#recons = pywt.waverec(coeffs,w)

fig, axs = plt.subplots(3,2)
axs[0,0].plot(coeffs[1])
axs[0,0].legend(['Level 1']);

axs[0,1].plot(coeffs[2])
axs[0,1].legend(['Level 2']);

axs[1,0].plot(coeffs[3])
axs[1,0].legend(['Level 3']);

axs[1,1].plot(coeffs[4])
axs[1,1].legend(['Level 4']);

axs[2,0].plot(coeffs[5])
axs[2,0].legend(['Level 5']);

axs[2,1].plot(recons)
axs[2,1].legend(['Reconstruction']);

plt.show;



#plt.figure()
#plt.plot(coeffs[1]);
#plt.legend(['Level 1'])
#plt.show;
#
#plt.figure()
#plt.plot(coeffs[2]);
#plt.legend(['Level 2'])
#plt.show;
#
#
#plt.figure()
#plt.plot(coeffs[3]);
#plt.legend(['Level 3'])
#plt.show;
#
#plt.figure()
#plt.plot(coeffs[4]);
#plt.legend(['Level 4'])
#plt.show;
#
#plt.figure()
#plt.plot(coeffs[5]);
#plt.legend(['Level 5'])
#plt.show;

# Plot Reconstruction of the signal 
#plt.figure()
#plt.plot(recons);
#plt.legend(['Reconstruction'])
#plt.show;




