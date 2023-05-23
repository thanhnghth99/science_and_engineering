import matplotlib.pyplot as plt
import numpy as np

# Constant number
T = 5
x_0 = 1
a = -1/T
t_start = 0
t_end = 25

# Differential equation
t = np.linspace(t_start, t_end, num=200, endpoint=True, retstep=False)
x_t = np.exp(a*t) * x_0

# Plot the solution x(t) in the time interval t = [0, 25]
plt.plot(t, x_t)
plt.title('Plot of the autonomous system in the time interval t = [0, 25]',
          fontsize = 13,
          fontweight = 'bold')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.axis([0, 25, 0, 1])
plt.grid()
plt.savefig('ex-5.5.1.png')
plt.show()