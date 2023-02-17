import matplotlib.pyplot as plt
import numpy as num
amp=3
fequency=6
t=num.arange(0,1,0.001)
x=amp*num.sin(2*num.pi*fequency*t)

plt.subplot(3,1,1)
plt.plot(t,x)
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Carrier signal")

u=[]
b=[0.2,0.4,0.6,0.8,1.0]
s=1
for i in t:
    if(i==b[0]):
        b.pop(0)
        if(s==0):
            s=1
        else:
            s=0
    u.append(s)

plt.subplot(3,1,2)
plt.plot(t,u)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Message Signal')

v=[]
for i in range(len(t)):
    if(u[i]==1):
        v.append(amp*num.sin(4*num.pi*fequency*t[i]))
    else:
        v.append(amp*num.sin(2*num.pi*fequency*t[i]))

plt.subplot(3,1,3)
plt.plot(t,v)
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("FSK signal")
plt.tight_layout()
plt.show()