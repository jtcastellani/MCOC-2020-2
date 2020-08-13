
from time import perf_counter
import scipy as sp
import scipy.linalg
import numpy as np

def mlp(N, dtype=sp.single):                    #obtenida del foro entrega GOLF
    matriz = np.zeros((N,N),dtype=dtype)
    np.fill_diagonal(matriz,2)
    for i in range(N):
        for j in range(N):
            if i+1 == j or i-1 == j:
                matriz[i][j] = -1
    return(matriz)

Ns = [
    2, 5, 10,
    12, 15, 20,
    30, 40, 45, 50, 55,
    60, 75, 100,
    125, 160, 200,
    250, 350, 500,
    600, 800, 1000,
    2000, 5000, 10000]


for e in range(10):
    
    Ts = []

    Mem = []

    name = (f"singletrue{e}.txt")

    fid = open(name,"w")
    
    for i in Ns:

        print(f"i = {i}")    
    
        A = mlp(i)
        
        t1 = perf_counter()

        scipy.linalg.inv(A, overwrite_a=True)
        
        t2 = perf_counter()

        dt = t2 - t1
        
        size = (i**2) * 28

        Ts.append(dt) 
        Mem.append(size)
    
        fid.write(f"{i} {dt} {size}\n")
    
        print(f"Tiempo transcurrido = {dt} s")
        print(f"Mmoria usada = {size} bytes")

        fid.flush()
    
    
fid.close()

