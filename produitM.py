"""
TP1:exo matrices
19/09/2023
Justin Biscarat-Aymes
Todo

"""

m1=[[1,0,0]
    [0,1,0]
    [0,0,1]]

m2=[[2,0,0]
    [0,2,0]
    [0,0,2]]

def ProduitM(m1,m2):
    if len(M1)==len(m2[0]):
        m=[]
        lM=len(m1[0])
        cM=len(m2)
        for i in range(lM-1):
            for j in range(cM-1):
                for k in range(len(m1)-1):
                    m[i][j]+= m1[i][k]*m2[k][j]
    return m

ProduitM(m1,m2)
        


