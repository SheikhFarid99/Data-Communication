import matplotlib.pyplot as plt
import numpy as np 
from math import pi

plt.close('all')

Fs = 2000 
t = np.arange(0,2,1/Fs)

Fc = 20 
Ac = 1 
c = Ac*np.cos(2*pi*Fc*t)
Fm = 2 
Am = 1

m = Am*np.sin(2*pi*Fm*t)
s = c * (1+m/Ac) 

plt.subplot(3,1,1)
plt.plot(t,c)
plt.title('carrier signal') 
plt.ylabel('Amplitude')
plt.xlabel('Time(s)');

plt.subplot(3,1,2)
plt.plot(t,m) 
plt.title('Message signal') 
plt.ylabel('Amplitude')
plt.xlabel('Time(s)');

plt.subplot(3,1,3)
plt.plot(t,s);
plt.title('modulation') 
plt.ylabel('Amplitude')
plt.xlabel('Time(s)');

plt.tight_layout()
plt.show()

