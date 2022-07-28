import matplotlib.pyplot as plt
import numpy as np

"""x = np.linspace(-10,9,20)
y = x ** 3
z = x ** 2

figure = plt.figure()

axes_cube = figure.add_axes([0.1,0.1,0.8,0.8])
axes_cube.plot(x,y,'b')
axes_cube.set_xlabel("X axis")
axes_cube.set_ylabel("Y axis")
axes_cube.set_title("Cube")

axes_Kare = figure.add_axes([0.13,0.6,0.20,0.18])
axes_Kare.plot(x,z,'r')
axes_Kare.set_xlabel("X axis")
axes_Kare.set_ylabel("Y axis")
axes_Kare.set_title("Kare")

plt.show()
"""

"""x = np.linspace(-10,9,20)
y = x ** 3
z = x ** 2

figure = plt.figure()
axes = figure.add_axes([0,0,1,1])
axes.plot(x,z,label= "Kare")
axes.plot(x,y,label="Küp")
axes.legend(loc = 1)


plt.show()"""

x = np.linspace(-10,9,20)
y = x ** 3
z = x ** 2

fig, axes = plt.subplot(2,1, figsize=(8,8)) #figsize figür boyutuu belirler.
axes[0].plot(x,y)
axes[0].set_title("kare")
axes[1].plot(x,z)
axes[1].set_titles("Küp")
plt.tight_layout()

fig.savefig("figure1.png")  #oluşturulan figürü dizin içine kaydeder.

plt.tight_layout()


plt.show()







