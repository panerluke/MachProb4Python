import numpy as np
import matplotlib.pyplot as plt

def prob4(h, v, theta, ax, ay):
    if h < 0:
        return print("The height should be above the ground!")
    if ay >= 0:
        return print("There would be no free fall!")
    
    y = np.array([(1/2)*ay, v*np.sin(theta * (np.pi/180)), h])
    
    t = np.roots(y)
    t = np.linspace(0, t[t > 0], 1000)
    
    y = np.polyval(y, t)
    y  = y[y >= 0]
    
    x = np.array([(1/2)*ax, v*np.cos(theta * (np.pi/180)), 0])
    x = np.polyval(x, t)
    x = x[0:(len(y))]
    
    xi = v*t*np.cos(theta * (np.pi/180))
    xi = xi[0:(len(y))]
    
    plt.plot(x, y)
    plt.plot(xi, y, '--')
    plt.legend(['non ideal motion', 'ideal motion'])
    plt.title('Projectile trajectory')
    plt.xlabel('Horizontal distance in m')
    plt.ylabel('Vertical distance in m')
    
    return