import scipy as sp
import matplotlib.pyplot as plt
import numpy as np

plt.figure()


plt.subplot(3, 1, 1)

for i in range(9):
    archivo = (f"halffalse{i}.txt")
    #file = "mimatmul{i}.txt"

    x = np.loadtxt(archivo, usecols=[0])
    y = np.loadtxt(archivo, usecols=[1])

    plt.loglog(x, y, 'o-')


plt.xlim(0, 20000)
plt.ylim(0, 3600)

yTicks = [0.1/1000, 1/1000, 10/1000, 0.1, 1, 10, 60, 600, 3600]
yTicks_Text = ["0.1 ms", "1 ms", "10 ms", "0.1 s", "1 s", "10 s", "1 min", "10 min", "1 hr"]

xTicks = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000]
plt.xticks(xTicks)

plt.yticks(yTicks, yTicks_Text)

frame1 = plt.gca()
frame1.axes.xaxis.set_ticklabels([])


plt.title("Rendimiento Scipy False, dtype=half", fontsize=14)
plt.ylabel("Tiempo transcurrido")


plt.grid(axis = 'both')



plt.subplot(3, 1, 2)

for i in range(9):
    archivo = (f"halftrue{i}.txt")
    #file = "mimatmul{i}.txt"

    x = np.loadtxt(archivo, usecols=[0])
    y = np.loadtxt(archivo, usecols=[1])

    plt.loglog(x, y, 'o-')


plt.xlim(0, 20000)
plt.ylim(0, 3600)

yTicks = [0.1/1000, 1/1000, 10/1000, 0.1, 1, 10, 60, 600, 3600]
yTicks_Text = ["0.1 ms", "1 ms", "10 ms", "0.1 s", "1 s", "10 s", "1 min", "10 min", "1 hr"]

xTicks = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000]
plt.xticks(xTicks)

plt.yticks(yTicks, yTicks_Text)

frame1 = plt.gca()
frame1.axes.xaxis.set_ticklabels([])


plt.title("Rendimiento Scipy True, dtype=half", fontsize=14)
plt.ylabel("Tiempo transcurrido")


plt.grid(axis = 'both')





plt.subplot(3, 1, 3)





y2 = np.loadtxt('halffalse0.txt', usecols=[2])
x2 = np.loadtxt('halffalse0.txt', usecols=[0])
plt.loglog(x2, y2, 'o-')


plt.xlim(0, 20000)
plt.ylim(0, 10**11)

xTicks = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000]
xTicks_Text = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000]

yTicks = [1000, 10000, 100000, 10**6, 10**7, 10**8, 10**9, 10**10, 10**11]
yTicks_Text = ["1 KB", "10 KB", "100 KB", "1 MB", "10 MB", "100 MB", "1 GB", "10 GB"]

plt.yticks(yTicks, yTicks_Text)
plt.xticks(xTicks, xTicks_Text)
plt.xticks(rotation=45)

plt.xlabel("Tamañano matriz N")
plt.ylabel("Uso de memoria")

plt.grid(axis = 'both')

plt.plot([0,16*10**9], [18000,16*10**9], 'black', linestyle="--")

plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=0.5)
plt.tight_layout()
plt.savefig('half.png', dpi=800)

plt.show()

