T=int(input())
for _ in range(T):
    N=int(input())
    hays=list(map(int,input().split()))
    if N==2:
        print(-1 if hays[0]!=hays[1] else hays[0])
        continue
    ans=set()
    for i in range(N-2):
        cur=hays[i]
        nexts=hays[i+1]
        nexter=hays[i+2]
        if cur==nexts or nexts==nexter:
            ans.add(nexts)
        elif cur==nexter:
            ans.add(cur)
    ans=sorted(ans)
    if len(ans)==0:
        print(-1)
    else:
        print(*ans)