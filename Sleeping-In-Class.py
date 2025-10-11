T=int(input())
for _ in range(T):
    N=int(input())
    sleep=list(map(int,input().split()))
    total=sum(sleep)
    #print(total)
    for length in range(N,0,-1):
        if total%length!=0:
            continue
        num=total/length
        cur=0
        flag=True
        for i in range(len(sleep)):
            #print(cur)
            cur+=sleep[i]
            if cur==num:
                cur=0
                continue
            if cur>num:
                flag=False
                break
        if not flag:
            continue
        print(N-length)
        break
