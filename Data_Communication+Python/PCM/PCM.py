import numpy as np
import matplotlib.pyplot as plt

# Sampling, quantization and coding

fsz = (7,5)                                                    # figure size
fsz2 = (fsz[0],fsz[1]/2.0)                                     # half high figure                                                             # initial parameters
Fs = 8000                                                      # sampling rate
fm = 1000                                                      # frequency of sinusoidal
tlen = 1.0                                                     # length in seconds
tt = np.arange(np.round(tlen*Fs))/float(Fs)                    # generate time axis
xt = np.sin(2*np.pi*fm*tt)                                     # generate sine

print('xt = {}'.format(xt[:12]))                               # print the first 12 values of x(t)

plt.figure(1, figsize=fsz)                                     # figure no 1 and its size
plt.plot(tt[:24], xt[:24])                                     # x-axis=tt , y-axis=xt
plt.grid()                                                     # showing girds
plt.show()                                                     # print base band sinusoidal

# create a labeled graph
plt.figure(2, figsize=fsz)                                     # figure no 2 and its size
plt.plot(tt[:24], xt[:24], '-b')                               # x-axis=tt , y-axis=xt ,color = blue
plt.plot(tt[:24], xt[:24], 'or', label='xt values')            # label the graph
plt.ylabel('$x(t)$')                                           # label y-axis
plt.xlabel('t [sec]')                                          # label x-axis
strt2 = 'Sinusoidal Waveform $x(t)$'
strt2 = strt2 + ', $f_m={}$ Hz, $F_s={}$ Hz'.format(fm, Fs)
plt.title(strt2)                                               # title of the graph
plt.legend()
plt.grid()                                                     # showing girds
plt.show()                                                     # print the labeled base band sinusoidal


fm = 500                                                       # frequency of sinusoid
phi=30
A=1.2
# make stem plot
plt.figure(3, figsize=fsz)
plt.stem(tt[:24], xt[:24],use_line_collection=True)
plt.ylabel('$x(t)$')
plt.xlabel('t [sec]')
strt1 = 'Stem Plot of Sinusoidal Waveform $x(t)$'
strt1 = strt1 + ', $f_m={}$ Hz, $F_s={}$ Hz'.format(fm, Fs)
plt.title(strt1)
plt.grid()
plt.show()

N = 3                                           # upsampling factor
xNt = np.vstack((xt, np.zeros((N-1, xt.size)))) # expand N times
xNt = np.reshape(xNt, -1, order='F')            # reshape into array
print(xNt[:24])                                 # check readout order
FsN = N*Fs                                      # new sampling rate
ttN = np.arange(xNt.size)/float(FsN)            # new time axis

# new stem plot
plt.figure(2, figsize=fsz)
plt.stem(ttN[:N*24], xNt[:N*24],use_line_collection=True)
plt.ylim([-1.2, 1.2])
plt.ylabel('$x_N(t)$')
plt.xlabel('t [sec]')
strt2 = 'Expanded by $N={}$ Sine Waveform $x_N(t)$'.format(N)
strt2 = strt2 + ', $f_m={}$ Hz, $F_{{sN}}={}$ Hz'.format(fm, FsN)
plt.title(strt2)
plt.grid()
plt.show()

def sinc_ipol(Fs, fL, k):
# create time axis
 ixk = int(np.round(Fs*k/float(2*fL)))
 tth = np.arange(-ixk, ixk+1)/float(Fs)
# sinc pulse
 ht = 2*fL*np.sinc(2*fL*tth)
 return tth, ht


# plot of interpolation waveform
fL = 3000                       # cutoff frequency
k = 10                          # sinc pulse truncation
tth, ht = sinc_ipol(FsN, fL, k)
plt.figure(3, figsize=fsz)
plt.plot(tth, ht, '-m')
plt.ylabel('$h(t)$')
plt.xlabel('t [sec]')
strt3 = "'sinc' Pulse for Interpolation"
strt3 = strt3 + ', $F_s={}$ Hz, $f_L={}$ Hz, $k={}$'.format(FsN, fL, k)
plt.title(strt3)
plt.grid()
plt.show()

# convolve expanded sine sequence with interpolation waveform to
# obtain upsampled (by factor N) sequence yNt with sampling rate FsN
yNt = np.convolve(xNt, ht, 'same')/float(Fs)
# stem plot of upsampled sequence
plt.figure(4, figsize=fsz)
plt.stem(ttN[:N*24], yNt[:N*24],use_line_collection=True)
plt.ylim([-1.2, 1.2])
plt.ylabel('$y_N(t)$')
plt.xlabel('t [sec]')
strt4 = 'Sine Waveform $y_N(t)$, Upsampled $N={}$'.format(N)
strt4 = strt4 + ', $f_m={}$ Hz, $F_{{sN}}={}$ Hz'.format(fm, FsN)
plt.title(strt4)
plt.grid()
plt.show()
