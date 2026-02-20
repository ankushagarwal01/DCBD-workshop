# Mex Grid Construction from CSES 
n = int(input())

k = 2*n-2
A = [[k]*n for _ in range(n)]
A[0][0] = 0
for d in range(1,n):
    for i in range(d+1):
        j = d  - i
        Ai = set(A[i][:j])
        Aj = set(A[j][:i])
        Aij = Ai | Aj
        A[i][j] = min(set(range(k)) - Aij)
for d in range(n,k +1):
    for i in range(d-n+1,n):
        j = d - i
        Ai = set(A[i][:j])
        Aj = set(A[j][:i])
        Aij = Ai | Aj
        A[i][j] = min(set(range(k)) - Aij)
for row in A:
    print(" ".join(map(str,row)))