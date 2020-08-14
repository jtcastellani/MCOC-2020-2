from time import perf_counter
import numpy as np
import scipy as sp
import scipy.linalg as splalg
from numpy import float32
from ploter import ploter 

names = ["A_invB.txt", "A_invBnpSolve.txt"]

ploter(names)

def mlp(N, dtype=float32):                    #obtenida del foro entrega GOLF
    matriz = np.zeros((N,N),dtype=dtype)
    np.fill_diagonal(matriz,2)
    for i in range(N):
        for j in range(N):
            if i+1 == j or i-1 == j:
                matriz[i][j] = -1
    return(matriz)

Ns = [
    2, 5, 10,
    20, 40,  60, 
    100, 
    160, 250, 
    350, 500, 1000, 2000,
    3000, 5000, 8000, 10000]


corridas = 10

tipos = ["A_invB.txt", "A_invBnpSolve.txt"]
archivos = [open(tipo, 'w') for tipo in tipos]

for i in Ns:
    
    tiempos = np.zeros((corridas, len(archivos)))
    print(f"i = {i}") 
    
    
    for e in range(corridas):

        print(f"e = {e}")    
    
        A = mlp(i)
        B = np.ones(i)

        t1 = perf_counter()
  
        A_inv = np.linalg.inv(A)  
        A_invB = A_inv*B
        
        t2 = perf_counter()

        t= t2 - t1
        tiempos[e][0] = t
        
        
        A = mlp(i)
        B = np.ones(i)

        t1 = perf_counter()
  
        A_invB = np.linalg.solve(A, B)
        
        t2 = perf_counter()

        t= t2 - t1
        tiempos[e][1] = t
        
    print("tiempos: ", tiempos)
    
    
    tiempos_x = [np.mean(tiempos[:,j]) for j in range(len(archivos))]

    print("tiempos promedios: ", tiempos_x)    
        
    for k in range(len(archivos)):
        archivos[k].write(f"{i} {tiempos_x[k]}\n")
        archivos[k].flush()
    
    
names = ["A_invB.txt", "A_invBnpSolve.txt"]

ploter(names)

