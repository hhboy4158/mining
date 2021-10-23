import numpy as np
import matplotlib.pyplot as plt


np.random.seed(7414)
x = np.random.rand(20) * 8 - 4
y = np.sin(x) + np.random.rand(20) * 0.2
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Generated Instances")
plt.grid()
plt.scatter(x, y, marker='x', c='red')

# plt.show()



weights = np.polyfit(x, y, 6)
print(weights)

f = np.poly1d(weights) #Build polynomial of degree 1
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Liner Regression")
plt.grid()
plt.scatter(x, y, marker='x', c='red')
gx = np.linspace(-4, 4, 100) #prepare 100 x values in range[-4, 4]
plt.plot(gx, f(gx), color='green') # draw line based on the gx and f()

plt.show()