import matplotlib.pyplot as plt
import numpy as np

angles = list(np.arange(0,(np.pi/4)+((np.pi/4)/100),(np.pi/4)/100)) #list of angles in radians
sin_angle = []

for angle in angles:
    sin_angle.append(np.sin(angle))
    
plt.plot(angles,sin_angle,label='y = sin(theta)')
plt.plot(angles,angles,label='y = theta')
plt.legend()
plt.ylabel('y')
plt.xlabel('theta (radians)')
plt.title('Comparing theta with sin(theta)')
plt.show()
