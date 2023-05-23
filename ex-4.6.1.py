import numpy as np
import matplotlib.pyplot as plt


x_start = 0
x_stop = 2*np.pi

x = np.linspace(x_start, x_stop, 100, endpoint=True, retstep=False)
y1 = np.sin(x)
y2 = np.cos(x)

# Define figure and axes objects
fig, ax = plt.subplots(1, 2, sharex = True, sharey = True)
fig.suptitle('sin(x) and cos(x) in 2 different plots',
             fontsize = 13,
             fontweight = 'bold')
plt.xlim(0, 2*np.pi)

# Plot sin()
plot1 = ax[0].plot(x, y1, 'g')
ax[0].set(title = 'sin(x) plot', xlabel = 'x', ylabel = 'y = sin(x)')
ax[0].grid()

# Plot cos()
plot2 = ax[1].plot(x, y2, 'r')
ax[1].set(title = 'cos(x) plot', xlabel = 'x', ylabel = 'y = cos(x)')
ax[1].grid()

label_list = ['y = sin(x)', 'y = cos(x)']
fig.legend([plot1, plot2],
           labels = label_list,
           loc = 1,                     #loc = 'upper right'
           borderaxespad = 1,
           title = 'legend title')
fig.tight_layout()
fig.savefig('ex-4.6.1.png')

plt.show()