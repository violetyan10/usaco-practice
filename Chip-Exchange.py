T=int(input())
for _ in range(T):
    A,B,cA,cB,fA=map(int,input().split())
    cur=B//cB*cA+A
    smallB=cB-1-B%cB
    bigA=fA-cur-1
    ans=0
    if cur>=fA:
        print(0)
        continue
    if cB>cA: #more Bs
        ans=smallB+bigA//cA*cB+bigA%cA
    if cA>=cB: #more As
        ans=smallB+bigA
    print(ans+1)