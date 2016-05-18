import matplotlib.pyplot as plt
plt.plot([2,4,6,8, 10], [1.5,2.8,4.4,5.9, 7.2], 'ro')
plt.plot([2,4,6,8, 10], [1.0,2.1,3.56,4.5, 5.0], 'bo')
plt.ylabel('Minutes')
plt.xlabel('Hundreds of Megabytes')
plt.axis([0,11, 0, 8])
plt.show()
