T=int(input())

for _ in range(T):
    N=int(input())
    log=list(map(int,input().split()))
    total=sum(log)

    for i in range(N,-1,-1):
        if total%i!=0:
            continue
        desir=total/i
        flag=True
        cur=0

        for j in range(len(log)):
            cur+=log[j]
            if cur==desir:
                cur=0
                continue
            if cur>desir:
                flag=False
                break
        if flag:
            print(N-i)
            break