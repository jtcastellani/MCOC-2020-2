  
def mimatmul(A,B):

    #print("Implementar matmul a mano")

  
    C = [[0 for x in range(len(A))] for y in range(len(A))]  
  

    for i in range(len(A)): 
        for j in range(len(B[0])): 
            for k in range(len(B)): 
  

                C[i][j] += A[i][k] * B[k][j] 
  
    #print (C)
    return (C)
