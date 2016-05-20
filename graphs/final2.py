import matplotlib.pyplot as plt
plt.plot([0.1,0.15, 0.2,0.5, 1, 1.2], [6.8,6.9,6.92, 6.95, 7.1, 7.3], 'ro')
plt.plot([0.1,0.15, 0.2, 0.5, 1,1.2], [2.8,3.3,3.94, 4.6, 6.95, 7.4], 'bo')

plt.ylabel('Minutes')
plt.xlabel('Millions of Key-Value Pairs')
plt.show()
