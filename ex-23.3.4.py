import matplotlib.pyplot as plt
import numpy as np


x_start = 0
x_stop = 2*np.pi

x = np.linspace(x_start, x_stop, 100, endpoint=True, retstep=False)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, 'g', label='y = sin(x)')
plt.plot(x, y2, 'r', label='y = cos(x)')
plt.title('sin(x) and cos(x)', fontsize=13, fontweight='bold')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(title='legend title', loc=0)
plt.grid()
plt.show()