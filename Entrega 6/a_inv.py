from time import perf_counter
import numpy as np
import scipy as sp
import scipy.linalg as splinalg
from numpy import float32
from ploter import ploter 


def mlp(N, dtype=float32):                    #script para crear la matriz laplaciana obtenida del foro entrega GOLF
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
    12000,  20000]


corridas = 10    #numero de repeteciones

tipos = ["A_invB.txt", "A_invBnpSolve.txt", "A_invBspSolve.txt", "A_invBspSolveSymPos.txt", "A_invBspSolveLower.txt", "A_invBspSolveOverwriteA.txt", "A_invBspSolveOverwriteB.txt", "A_invBspSolveCheckFinite.txt", "A_invBspSolveTransposed.txt"]       #se crean un txt por tipo de solucion y luego se escriben
archivos = [open(tipo, 'w') for tipo in tipos]

for i in Ns:   #ciclo for para recorrer los distintos tamaños de matrices
    
    tiempos = np.zeros((corridas, len(archivos)))   #matriz de tiempos de cada corrida en las filas y una columna por tipo de solucion
    print(f"i = {i}") 
    
    
    for e in range(corridas):     #ciclo for para recorrer las corridas

        print(f"e = {e}")    
    
    #inversion de la matriz A para luego multiplicarla por B
        A = mlp(i)
        B = np.ones(i)

        t1 = perf_counter()
  
        A_inv = np.linalg.inv(A)  
        A_invB = A_inv*B
        
        t2 = perf_counter()

        t= t2 - t1
        tiempos[e][0] = t
        
    #solucion por medio de numpy    
        A = mlp(i)
        B = np.ones(i)

        t1 = perf_counter()
  
        A_invB = np.linalg.solve(A, B)
        
        t2 = perf_counter()

        t= t2 - t1
        tiempos[e][1] = t
        
    #Soluciones desde scipy
        A = mlp(i)
        B = np.ones(i)

        t1 = perf_counter()
  
        A_invB = splinalg.solve(A, B, sym_pos = True)
        
        t2 = perf_counter()

        t= t2 - t1
        tiempos[e][2] = t
        
        A = mlp(i)
        B = np.ones(i)

        t1 = perf_counter()
  
        A_invB = splinalg.solve(A, B, lower = True)
        
        t2 = perf_counter()

        t= t2 - t1
        tiempos[e][3] = t
        
        
        A = mlp(i)
        B = np.ones(i)

        t1 = perf_counter()
  
        A_invB = splinalg.solve(A, B, overwrite_a = True)
        
        t2 = perf_counter()

        t= t2 - t1
        tiempos[e][4] = t
        
        
        A = mlp(i)
        B = np.ones(i)

        t1 = perf_counter()
  
        A_invB = splinalg.solve(A, B, overwrite_b = True)
        
        t2 = perf_counter()

        t= t2 - t1
        tiempos[e][5] = t
        
        
        A = mlp(i)
        B = np.ones(i)

        t1 = perf_counter()
  
        A_invB = splinalg.solve(A, B, overwrite_b = True)
        
        t2 = perf_counter()

        t= t2 - t1
        tiempos[e][6] = t
        
        
        A = mlp(i)
        B = np.ones(i)

        t1 = perf_counter()
  
        A_invB = splinalg.solve(A, B, check_finite = True)
        
        t2 = perf_counter()

        t= t2 - t1
        tiempos[e][7] = t
        
            
        A = mlp(i)
        B = np.ones(i)

        t1 = perf_counter()
  
        A_invB = splinalg.solve(A, B, transposed = True)
        
        t2 = perf_counter()

        t= t2 - t1
        tiempos[e][8] = t
        
        
           
               
        
        
        
    print("tiempos: ", tiempos)
    
    
    tiempos_x = [np.mean(tiempos[:,j]) for j in range(len(archivos))]  #se registran los tiempos promedios para cada caso

    print("tiempos promedios: ", tiempos_x)    
        
    for k in range(len(archivos)):      #registra el N de la matriz junto a su tiempo promedio
        archivos[k].write(f"{i} {tiempos_x[k]}\n")
        archivos[k].flush()
   

names = ["A_invB.txt", "A_invBnpSolve.txt", "A_invBspSolve.txt", "A_invBspSolveSymPos.txt", "A_invBspSolveLower.txt", "A_invBspSolveOverwriteA.txt", "A_invBspSolveOverwriteB.txt", "A_invBspSolveCheckFinite.txt", "A_invBspSolveTransposed.txt"]    #se declarn los tipos de archivos para luego graficarlos

ploter(names)

