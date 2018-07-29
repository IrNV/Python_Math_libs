import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

x = np.arange(0, 10, 2)
y = np.exp(-x / 3.0)

f = interpolate.interp1d(x, y, kind="quadratic")  # Задаем интерполяцию данных
xnew = np.arange(0, 8, 1)
ynew = f(xnew)

plt.plot(x, y, "o", xnew, ynew, "-")  # Выводим результат
plt.show()

