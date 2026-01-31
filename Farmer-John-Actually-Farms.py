T=int(input())
for _ in range(T):
    N=int(input())
    initH=list(map(int,input().split()))
    grow=list(map(int,input().split()))
    request=list(map(int,input().split()))
    order=[i for i in range(N)]
    order=sorted(order, key=lambda x:request[x])
    days=0
    for i in range(N-1):
        first=order[i]
        second=order[i+1]
        if initH[first]<initH[second] and grow[first]>grow[second]:
            need=(initH[second]-initH[first]+grow[first]-grow[second])//(grow[first]-grow[second])
            days=max(days,need)
    for j in range(N):
        initH[j]+=grow[j]*days
    for a in range(N-1):
        first=order[a]
        second=order[a+1]
        if initH[first]<=initH[second]:
            days=-1
    print(days)