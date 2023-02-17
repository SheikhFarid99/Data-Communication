import matplotlib.pylab as plt
import numpy as num

fequency=10 
amp=3
t=num.arange(0,1,0.001)
x=amp*num.sin(2*num.pi*fequency*t)
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
v=[]
for i in range(len(t)):
    if u[i]==0:
        v.append(num.sin(2*num.pi*fequency*t[i]))
    else:
        v.append(amp*num.sin(2*num.pi*fequency*t[i]))
    
    
plt.subplot(3,1,1)
plt.plot(t,x)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Carrier signal')

plt.subplot(3,1,2)
plt.plot(t,u)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Square wave')

plt.subplot(3,1,3)
plt.plot(t,v)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('ASK Signal')
plt.tight_layout()
plt.show()