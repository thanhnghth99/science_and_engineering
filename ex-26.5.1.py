import matplotlib.pyplot as plt
import numpy as np


b = 1
p = 0.5

T_s = 0.01
T_stop = 1
x_k = 100
N = int(T_stop/T_s)
data = []
data.append(x_k)

for k in range(N):
    x_k1 = x_k + T_s * (b * x_k - p * x_k**2)
    x_k = x_k1
    data.append(x_k1)

t = np.linspace(0, T_stop, num=101, endpoint=True, retstep=False)
plt.plot(t, data, 'g')
plt.title('Simulation of Bacteria Population')
plt.xlabel('t[s]')
plt.ylabel('x')
plt.grid()
plt.savefig('ex-26.5.1.png')
plt.show()