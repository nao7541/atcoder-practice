N, X= map(int, input().split())
A = list(map(int, input().split()))
ans = []

""" for i in range(len(A)): 
    if A[i] != X: ans.append(str(A[i]))
    
ans = ' '.join(ans)
print(ans) """
print(" ".join([str(i) for i in A if i != X]))