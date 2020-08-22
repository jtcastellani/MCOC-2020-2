import scipy as sp
import matplotlib.pyplot as plt
import numpy as np

plt.figure()

Ns = np.array([0,2, 5, 10,
    20, 40,  60, 
    100, 
    160, 250, 
    350, 500, 1000,
    3000, 5000, 8000,  12000])    


plt.subplot(2, 1, 1)

for i in range(5):
    archivo = (f"SolveD{i}.txt")

    x = np.loadtxt(archivo, usecols=[0])
    ens = np.loadtxt(archivo, usecols=[1])


    plt.loglog(x, ens, 'o-', color="gray")


plt.ylim(0.00001, 60)

yTicks = [0.1/1000, 1/1000, 10/1000, 0.1, 1, 10, 60, 600]
yTicks_Text = ["0.1 ms", "1 ms", "10 ms", "0.1 s", "1 s", "10 s", "1 min", "10 min"]

xTicks = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000]
plt.xticks(xTicks)

plt.yticks(yTicks, yTicks_Text)


plt.ylabel("Tiempo de ensamblado")

const1 =   [25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 24, 24, 24, 24, 24, 24, 24]
const2 =   [0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01]

plt.loglog(Ns, const1, "b--")    
plt.loglog(Ns, (Ns)*25/12000, "--", color="orange")
plt.loglog(Ns, (Ns**2)*25/12000**2, "g--")
plt.loglog(Ns, (Ns**3)*25/12000**3, "r--")
plt.loglog(Ns, (Ns**4)*25/12000**4, "m--")




plt.subplot(2, 1, 2)

for i in range(5):
    archivo = (f"SolveD{i}.txt")

    x = np.loadtxt(archivo, usecols=[0])
    sol = np.loadtxt(archivo, usecols=[2])

    plt.loglog(x, sol, 'o-', color="gray")



plt.ylim(0.00001, 60)

plt.loglog(Ns, const2, "b--")    
plt.loglog(Ns, (Ns)*0.01/12000, "--", color="orange")
plt.loglog(Ns, (Ns**2)*0.01/12000**2, "g--")
plt.loglog(Ns, (Ns**3)*0.01/12000**3, "r--")
plt.loglog(Ns, (Ns**4)*0.01/12000**4, "m--")

yTicks = [0.1/1000, 1/1000, 10/1000, 0.1, 1, 10, 60, 600]
yTicks_Text = ["0.1 ms", "1 ms", "10 ms", "0.1 s", "1 s", "10 s", "1 min", "10 min"]

xTicks = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000]


plt.yticks(yTicks, yTicks_Text)
plt.xticks(xTicks, xTicks, rotation = 45)

plt.ylabel("Tiempo de solución")
plt.xlabel("Tamaño matriz N")
plt.xticks(xTicks, xTicks, rotation = 45)








plt.tight_layout()
plt.savefig('SolveD.png', dpi=300)

plt.show()