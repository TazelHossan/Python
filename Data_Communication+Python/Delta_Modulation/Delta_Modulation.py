# Delta Modulation

import numpy as np
import matplotlib.pyplot as plt
import pylab as pl

#fsz = (7,5)                                 # figure size
Fs = 80                                     # sampling rate
fm = 10                                     # frequency of sinusoid
tlen = 1.0                                  # length in seconds

tt = np.arange(np.round(tlen*Fs))/float(Fs) # generate time axis
xt = np.sin(2*np.pi*fm*tt)                  # generate a sine wave:

pl.subplot(2,1,1)
pl.title('$Delta Modulation Technique$')
pl.xlabel('Figure:Modulated Signal')
pl.plot(xt,'-k',label='cosine')
pl.legend(loc='best')

l=len(xt)
delta=1                                     # define step size and plot the delta modulated signal
xn=[0,0]
d=[]

for i in range(1,l):
    if xt[i]>xn[i]:
        d.append(1)
        xn.append(xn[i]+delta)
    else:
        d.append(0)
        xn.append(xn[i]-delta)
x = np.arange(l+1)

plt.step(x,xn ,where='mid', label='mid')
plt.plot(x, xn, 'C3o', alpha=1)


                                            # recover the original signal (apply demodulation)
for i in range(1,len(d)):
    if d[i]>xn[i]:
        d.append(0)
        xn.append(xn[i]-delta)
    else:
        d.append(1)
        xn.append(xn[i]+delta)

pl.subplot(2,1,2)
pl.xlabel('Figure:Recovered Original Signal')
pl.plot(xt,'r',label='original signal')
pl.legend(loc='best')
plt.grid()
plt.show()
