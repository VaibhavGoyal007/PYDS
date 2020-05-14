import matplotlib.pyplot as plt
import numpy as np

def graph(s_x,e_x):
    x = np.linspace(s_x,e_x)
    plt.plot(x,np.log2(x))
    plt.plot(x,0.5*x-1)
    plt.show()

x1,x2 = map(int,input("Enter the range of x seprated by a space: ").split())
graph(x1,x2)

