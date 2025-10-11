N,M=map(int,input().split())

cows=[]
for _ in range(N):
    s,t,c=map(int,input().split())
    cows.append([s-1,t-1,c])

air_conds=[]
for _ in range(M):
    a, b, p, m=map(int,input().split())
    air_conds.append([a-1,b-1,p,m])

min_cost = 100000000000000000000000000 

def conditioning(index, cur_cost, cool):
    global min_cost
    if index == M:
        for s, t, c in cows:
            for i in range(s,t+1):
                if cool[i]<c:
                    return
        min_cost=min(min_cost, cur_cost)  
        return
    #not use
    conditioning(index+1, cur_cost, cool[:])

    #uses
    a, b, p, cost=air_conds[index]
    new_cooling=cool[:]
    for i in range(a, b + 1):
        new_cooling[i]+= p
    conditioning(index+1, cur_cost+cost, new_cooling)

initial_cooling = [0] * 101

conditioning(0, 0, initial_cooling)

print(min_cost)