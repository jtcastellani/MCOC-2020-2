import scipy as sp
import matplotlib.pyplot as plt
import numpy as np

def ploter(nombres):
    xtks =[
    2, 5, 10,
    20, 40,  60, 
    100, 
    160, 250, 
    350, 500, 1000, 2000,
    3000, 5000, 8000, 
    12000,  20000]
    
    ytks = [0.1/1000, 1/1000, 10/1000, 0.1, 1, 10, 60, 600]
    ytks_text = ["0.1 ms", "1 ms", "10 ms", "0.1 s", "1 s", "10 s", "1 min", "10 min"]


    plt.figure()
    
    for nombre in nombres:
        datos = np.loadtxt(nombre)
        Ns = datos[:, 0]
        tiempos = datos[:, 1]
        
        print("Ns: ", Ns)
        print("tiempos: ", tiempos)
        
        plt.loglog(Ns,tiempos, "-o", label = nombre)
        plt.ylabel("Tiempo transcurrido")
        plt.xlabel("Tamaño matriz N")
        plt.grid(True)
        plt.xticks(xtks, xtks, rotation = 45)
        plt.yticks(ytks, ytks_text)
        
    plt.tight_layout()
    plt.legend()
    plt.savefig("entrega_5.png", dpi = 300)
    plt.show()


