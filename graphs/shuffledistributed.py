import matplotlib.pyplot as plt
plt.plot([1,2,3,4, 5], [0.78,1.7,2.7,3.9, 5.1], 'ro')
plt.plot([1,2,3,4, 5], [0.63,1.3,2.0,2.7, 3.3], 'bo')

plt.axis([0,6, 0, 6])
plt.ylabel('Minutes')
plt.xlabel('Gigabytes')
plt.show()
