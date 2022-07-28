import matplotlib.pyplot as plt
import numpy as np

"""
plt.title("Kare Grafiği")   #Grafik başlığı
plt.xlabel("X-Ekseni")  # x-eksen etiketi 
plt.ylabel("Y-Ekseni")  #y-eksen etiketi
x = [1,2,3,4]   #x- ekseni degerleri
y = [1,4,9,16]  #y- ekseni degerleri
plt.axis([-1,10,0,20])  #x-y eksenlen aralıkları
plt.plot(x,y,color="blue",linewidth="3")    #Grafik çizgisi özellikleri

plt.plot(x,y)   #grafiği oluştur
plt.show()  #Grafiği göster
"""

"""plt.title("Kuvvet Grafiği")
x= np.linspace(0,2,100) #ekseni 0-100 arasını 2'şerli aralıklara bölme
plt.plot(x, x, label = "Doğrusal", color = "blue", linewidth ="3")
plt.plot(x, x*x, label = "Kare", color = "yellow", linewidth ="3.5")
plt.plot(x, x**3, label = "Küp", color = "green", linewidth ="4")

plt.xlabel("x ekseni")
plt.ylabel("y ekseni")

plt.legend()
plt.show()
"""

"""x= np.linspace(0,2,100)
fig, axs = plt.subplots(3)

axs[0].plot(x, x, color = "blue", linewidth ="3")
axs[0].set_title("doğrusal")

axs[1].plot(x, x*x, color = "yellow", linewidth ="3.5")
axs[1].set_title("doğrusal")

axs[2].plot(x, x**3, color = "green", linewidth ="4")
axs[2].set_title("doğrusal")

plt.tight_layout()  #grafikler arası boşluk oluşturur
plt.legend
plt.show()"""

x= np.linspace(0,2,100)
fig, axs = plt.subplots(3,3)

axs[0,1].plot(x, x, color = "blue", linewidth ="3")
axs[0,1].set_title("doğrusal")

axs[1,0].plot(x, x*x, color = "yellow", linewidth ="3.5")
axs[1,0].set_title("doğrusal")

axs[2,0].plot(x, x**3, color = "green", linewidth ="4")
axs[2,0].set_title("doğrusal")

axs[1,2].plot(x, x**-2, color = "green", linewidth ="4")
axs[1,2].set_title("Karekök")
axs[2,2].plot(x, x**-3, color = "green", linewidth ="4")
axs[2,2].set_title("Küpkök")
fig.delaxes(axs[0][0])
fig.delaxes(axs[0][2])
fig.delaxes(axs[1][1])
fig.delaxes(axs[2][1])
plt.tight_layout()  #grafikler arası boşluk oluşturur
plt.show()



