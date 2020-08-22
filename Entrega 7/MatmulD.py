from time import perf_counter
import numpy as np
from numpy import double

from scipy.linalg import solve as spsolve, inv as spinv
from scipy.sparse.linalg import inv as SparseInv, spsolve as SparseSolve
from scipy.sparse import csr_matrix as disp


def mlp(N, dtype=double):                 #script para crear la matriz laplaciana obtenida del foro entrega GOLF
    matriz = np.zeros((N,N),dtype=dtype)
    np.fill_diagonal(matriz,2)
    for i in range(N):
        for j in range(N):
            if i+1 == j or i-1 == j:
                matriz[i][j] = -1
    return(matriz)


Ns = [                     #tamaño de las matrices
    2, 5, 10,
    20, 40,  60, 
    100, 
    160, 250, 
    350, 500, 1000, 2000,
    3000, 5000, 8000, 
    12000]
    

for e in range(5):
    
    Te = []

    Ts = []

    name = (f"MatmulD{e}.txt")

    fid = open(name,"w")
    
    for i in Ns:

        print(f"i = {i}")    
    
        t1 = perf_counter()
       
        A = disp(mlp(i))
        B = disp(mlp(i))
        
        t2 = perf_counter()
        
        C = A@B
        
        t3 = perf_counter()
        

        ens = t2 - t1
        sol = t3 - t2
        

        Te.append(ens) 
        Ts.append(sol)
    
        fid.write(f"{i} {ens} {sol}\n")
    

        fid.flush()
    
    
fid.close()