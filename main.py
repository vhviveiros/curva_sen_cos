import numpy as np
import matplotlib.pyplot as plot

x = np.arange(0, 5 * np.pi, 0.1)
y = np.sin(x)
z = np.cos(x)

plot.plot(x, y, x, z)

plot.xlabel('Valores de x')  # string must be enclosed with quotes '  '
plot.ylabel('sen(x) e cos(x)')
plot.title("Sen(x) x Cos(x)")
plot.legend(['sen(x)', 'cos(x)'])

plot.show()