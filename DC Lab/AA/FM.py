import numpy as np
import matplotlib.pyplot as plt
from math import pi

Fs = 2000 

t = np.arange(0,0.2,1/Fs) 


Fc = 100 
Fm = 10 

index = 3 

frm = np.cos(2*pi*Fc*t + index*np.sin(2*pi*Fm*t)) 

m = np.sin(2*pi*Fm*t) ;

plt.plot(t,frm) ;
plt.title('Frequency Modulated Single') ;
plt.xlabel('Time(s)')
plt.ylabel('Amplitude')

plt.plot(t,m) 

plt.legend(['FM signal','Message Signal'])
plt.show()