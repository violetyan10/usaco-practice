T,k=map(int,input().split())
for _ in range(T):
    N=int(input())
    S=input().strip()
    ans=[1]*3*N
    if N%2==1:
        print(-1)
        continue
    halves=True
    for i in range(3*N//2):
        if S[i]!=S[i+3*N//2]:
            halves=False
            break
    if halves:
        print(1)
        print(*ans)
        continue
    for i in range(N//2):
        right=S[i*3:i*3+3]
        left=S[(i+N//2)*3:(i+N//2)*3+3]
        if right!=left:
            #COW
            #WCO
            #OWC
            if right[:2]==left[1:]:
                ans[i*3+2]=2
                ans[(i+N//2)*3]=2
            if left[:2]==right[1:]:
                ans[i*3]=2
                ans[(i+N//2)*3+2]=2
    print(max(ans))
    print(*ans)
