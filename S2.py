import matplotlib
import matplotlib.pyplot as plt
x = [1,6,3]
y = [5,9,4]

x2 = [1,2,3]
y2 = [10,14,12]

plt.plot(x, y, label='First Line')
plt.plot(x2, y2, label='Second Line')
plt.xlabel('Plot Number')
plt.ylabel('Important var')
plt.title('Interesting Graph Check it out')
plt.legend()
plt.show()