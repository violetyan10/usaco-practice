N=int(input())

A=list(map(int,input().split()))
B=list(map(int,input().split()))

moves=0

for i in range(N):
    val=B[i] #corect val
    index=A.index(val) #where it is curr

    if index>i:
        moves+=1
    # if B[i]==A[i]:
    #     continue
    # val=B[i] #corect val
    # index=A.index(val) #where it is curr
    # moves+=1
    # A.insert(i,val)
    # A.pop(index+1)
    # if A==B:
    #     break
#print(A)
print(moves)