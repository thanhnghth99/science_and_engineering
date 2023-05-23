import matplotlib.pyplot as plt
import numpy as np


b = 1
p = 0.5

T_s = 0.02
T_start = -1
T_stop = 1
x1_k = 1
x2_k = 1
N = int((T_stop-T_start)/T_s)
data_x1 = []
data_x2 = []
data_x1.append(x1_k)
data_x2.append(x2_k)

for k in range(N):
    x1_k1 = x1_k - T_s * x2_k
    x2_k1 = x2_k + T_s * x1_k
    
    x1_k = x1_k1
    x2_k = x2_k1
    
    data_x1.append(x1_k1)
    data_x2.append(x2_k1)

t = np.linspace(T_start, T_stop, num=101, endpoint=True, retstep=False)
plt.plot(t, data_x1, 'g', label='dx1/dt = -x2')
plt.plot(t, data_x2, 'b', label='dx2/dt = x1')
plt.title('Simulation of 2 Variables')
plt.xlabel('t[s]')
plt.ylabel('x')
plt.grid()
plt.legend(loc = 3) #lower left
plt.savefig('ex-26.5.2.png')
plt.show()