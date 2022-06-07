import matplotlib
import matplotlib.pyplot as plt
labels=['Python','C','C++','PHP','Java','Ruby']
sizes=[33,52,12,17,42,48]
separated=(.1,0,0,0,0,0)
plt.pie(sizes,labels=labels,autopct='%1.1f%%',explode=separated)
plt.axis('equal')
plt.show()