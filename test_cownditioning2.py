N,M=map(int,input().split())

cows=[]
for _ in range(N):
    s,t,c=map(int,input().split())
    cows.append([s-1,t-1,c])

air_conds=[]
for _ in range(M):
    a, b, p, m=map(int,input().split())
    air_conds.append([a-1,b-1,p,m])

#binary
min_cost = 1189734681264164163481364812648126387413846831461874

max_mask=2**M
for mask in range(max_mask): #going through all subsets of ac on or off
    cost=0
    cooling=[0]*101
    cur=1
    for i in range (M):
        if cur & mask:
            a, b, p, c=air_conds[i]
            for j in range(a, b + 1):
                cooling[j]+= p
            cost+=c
        cur=cur<<1
    flag=True
    for s,t,c in cows:
        for i in range(s,t+1):
            if cooling[i]<c:
                flag=False
                break
        if flag==False:
            break
    if flag:
        min_cost=min(min_cost,cost)

print(min_cost)