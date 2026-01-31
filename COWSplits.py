def solve_case(N,S,k):
    if N%2==1:
        return -1

    blocks=[S[i:i+3] for i in range(0,3*N,3)]

    if blocks[:N//2]==blocks[N//2:]:
        return 1,[1]*(3*N)

    op_id=[]
    for i in range(N):
        if i<N//2:
            op_id.extend([1,1,1])
        else:
            op_id.extend([2,2,2])

    return 2,op_id

T,k=map(int,input().split())
for _ in range(T):
    N=int(input())
    S=input().strip()
    result=solve_case(N,S,k)
    if result==-1:
        print(-1)
    else:
        M,op_id=result
        print(M)
        print(" ".join(map(str, op_id)))
