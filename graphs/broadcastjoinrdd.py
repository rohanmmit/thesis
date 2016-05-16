import matplotlib.pyplot as plt
plt.plot([1,2.5,5,7.5, 10, 10.06], [1.3,1.5,1.56,1.6, 1.7, 1.76], 'ro')
plt.plot([1,2.5,5,7.5, 10, 10.06], [0.55,0.75,1,1.2, 1.5, 2.15], 'bo')
plt.ylabel('Minutes')
plt.xlabel('Millions of Key-Pairs')
plt.show()
