from scipy import matmul, rand, savetxt
from time import perf_counter
import numpy as np
from mimatmul import mimatmul

Ns = [
    2, 5, 10,
    12, 15, 20,
    30, 40, 45, 50, 55,
    60, 75, 100,
    125, 160, 200,
    250, 350, 500,
    600, 800, 1000,]


for e in range(9):
    
    Ts = []

    Mem = []

    name = (f"mimatmul{e}.txt")

    fid = open(name,"w")
    
    for i in Ns:

        print(f"i = {i}")    
    
        A = rand(i,i)
        B = rand(i,i)

        t1 = perf_counter()
#     C = A@B   
        C = mimatmul(A,B)     
        t2 = perf_counter()

        dt = t2 - t1
        size = 3 * (i**2) * 8 

        Ts.append(dt) 
        Mem.append(size)
    
        fid.write(f"{i} {dt} {size}\n")
    
        print(f"Tiempo transcurrido = {dt} s")
        print(f"Mmoria usada = {size} bytes")

        fid.flush()
    
    
fid.close()





