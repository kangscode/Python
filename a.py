import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3]
y = [-1, -2, -3]
plt.plot(x, y)
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

x = np.arange(-10,11)
plt.bar(x, - x**2)
plt.show()

x = np.random.rand(500)
y = np.random.rand(500)
colors = np.random.randint(0, 100, 500)
sizes = np.pi * 1000 * np.random.rand(500)
plt.scatter(x, y, c=colors, s=sizes, alpha=0.5)
plt.show()

data = np.random.randn(1000)
plt.hist(data, bins=50, normed=True, color='g')
plt.show()

fig, (ax1, ax2) = plt.subplots(1, 2)
x = [1, 2, 3]
y = [-1, -2, -3]
ax1.plot(x, y)
ax1.xlabel("X")
ax1.ylabel("Y")
x = np.arange(-10,11)
ax2.bar(x, - x**2)
fig.show()

x = np.random.random((1000, 1000))
x.imshow(x)


x = np.arange(-10,11)
y1 = x**2
y2 = 2*x
plt.plot(x, y1, x, y2)
plt.xlabel("X")
plt.ylabel("Y")
plt.show()


a=""
a="dks"
print(a)

