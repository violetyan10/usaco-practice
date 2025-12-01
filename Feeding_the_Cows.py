T=int(input())
for _ in range(T):
    N,K=list(map(int, input().split()))
    cows=input()
    patches=0
    gs=[0 for _ in range(N)]
    hs=[0 for _ in range(N)]
    ans=["." for _ in range(N)]
    for i in range(N):
        if cows[i]=="G":
            if gs[i]!=1:
                patches+=1
                for j in range(i,min(N,i+2*K+1)):
                    gs[j]=1
                if ans[min(N-1,i+K)]==".":
                    ans[min(N-1,i+K)]="G"
                else:
                    ans[min(N-1,i+K)-1]="G"
        else:
            if hs[i]!=1:
                patches+=1
                for j in range(i,min(N,i+2*K+1)):
                    hs[j]=1
                if ans[min(N-1,i+K)]==".":
                    ans[min(N-1,i+K)]="H"
                else:
                    ans[min(N-1,i+K)-1]="H"
    print(patches)
    print("".join(ans))