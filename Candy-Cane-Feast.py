N,M=map(int,input().split())
cowH=list(map(int,input().split()))
caneH=list(map(int,input().split()))
for cane in caneH:
    height=0
    for i in range(N):

        cow=cowH[i]
        if cow>height:
            if cow>cane:
                cowH[i]+=cane-height
                height=cane
                break
            cowH[i]+=cow-height
            height=cow
for cow in cowH:
    print(cow)      
