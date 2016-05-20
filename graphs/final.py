import matplotlib.pyplot as plt
plt.plot([25,35,45,55], [19,3.86,2.84, 2.06], 'ro')
plt.plot([25, 35, 45, 55], [5.62,2.68,2.2,2.15], 'bo')

plt.axis([24,56, 0, 20])
plt.ylabel('Minutes')
plt.xlabel('Number of Partitions')
plt.show()
