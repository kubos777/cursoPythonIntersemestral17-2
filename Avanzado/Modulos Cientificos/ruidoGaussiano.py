"""
Simple image blur by convolution with a Gaussian kernel
"""

import numpy as np
from scipy import fftpack
import matplotlib.pyplot as plt

# leer la imagen
img = plt.imread('../../data/imagen.png')

# Creando un kernerl gausiano de convolusion de 1-D
t = np.linspace(-10, 10, 30)
bump = np.exp(-0.1*t**2)
bump /= np.trapz(bump) # normalizar la integral a 1

# hacer un kernerl 2-D de este
kernel = bump[:, np.newaxis] * bump[np.newaxis, :]

# fourier transfor con la mimsa imagen
kernel_ft = fftpack.fft2(kernel, shape=img.shape[:2], axes=(0, 1))

# convolve
img_ft = fftpack.fft2(img, axes=(0, 1))
img2_ft = kernel_ft[:, :, np.newaxis] * img_ft
img2 = fftpack.ifft2(img2_ft, axes=(0, 1)).real

img2 = np.clip(img2, 0, 1)

# Graficar
plt.imshow(img2)
plt.show()
