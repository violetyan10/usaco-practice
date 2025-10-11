import sys

sys.stdin = open("speeding.in", "r")
sys.stdout = open("speeding.out", "w")

N,M = map(int, sys.stdin.readline().split())
road=[]
bessie=[]
for _ in range(N):
    road.append(list(map(int, sys.stdin.readline().split())))
for _ in range(M):
    bessie.append(list(map(int, sys.stdin.readline().split())))

#testing trying to make everything easier :(
for a in range(1,N):
    road[a][0]+=road[a-1][0]
for b in range(1,M):
    bessie[b][0]+=bessie[b-1][0]


max_over=0
for i in range(100): #simulates each mile
    cur=0
    lim=0
    for j in range(N):
        if i<road[j][0]:
            lim=road[j][1]
            break
    for k in range(M):
        if i<bessie[k][0]:
            cur=bessie[k][1]
            break
    cur_max=cur-lim
    if cur_max>max_over:
        max_over=cur_max
print(max_over)