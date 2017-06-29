import numpy as np
from scipy import fftpack
import pylab as pl

#Inicializamos una semilla pseudoaletorios
np.random.seed(1234)

#Definimos los intervalos de tiempo y el periodo
time_step = 0.02
period = 5.
#Definimos el vector de tiempo
time_vec = np.arange(0, 20, time_step)
#Y la funcion a transformar
sig = np.sin(2 * np.pi / period * time_vec) + \
      0.5 * np.random.randn(time_vec.size)

sample_freq = fftpack.fftfreq(sig.size, d=time_step)
#Obtenemos la transformada
sig_fft = fftpack.fft(sig)
pidxs = np.where(sample_freq > 0)
freqs, power = sample_freq[pidxs], np.abs(sig_fft)[pidxs]
freq = freqs[power.argmax()]

pl.figure()
pl.plot(freqs, power)
pl.xlabel('Frequency [Hz]')
pl.ylabel('plower')
axes = pl.axes([0.3, 0.3, 0.5, 0.5])
pl.title('Peak frequency')
pl.plot(freqs[:8], power[:8])
pl.setp(axes, yticks=[])


