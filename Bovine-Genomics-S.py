import sys

sys.stdin = open("cownomics.in", "r")
sys.stdout = open("cownomics.out", "w")

N,M = map(int, sys.stdin.readline().split())
spotty=[]
plain=[]
for _ in range(N):
    cows=[]
    spots=sys.stdin.readline().strip()
    for spot in spots:
        if spot=="A":
            cows.append(0)
        if spot=="C":
            cows.append(1)
        if spot=="G":
            cows.append(2)
        if spot=="T":
            cows.append(3)
    spotty.append(cows)   
for _ in range(N):
    cows=[]
    spots=sys.stdin.readline().strip()
    for spot in spots:
        if spot=="A":
            cows.append(0)
        if spot=="C":
            cows.append(1)
        if spot=="G":
            cows.append(2)
        if spot=="T":
            cows.append(3)
    plain.append(cows)  

ans=0

for i in range(M):
    for j in range(i+1,M):
        for k in range(j+1,M):
            spotty_trios=set()
            plain_trios=set()

            for cow in spotty:
                triplet=(cow[i], cow[j], cow[k])
                spotty_trios.add(triplet)

            for cow in plain:
                triplet=(cow[i], cow[j], cow[k])
                plain_trios.add(triplet)

            if spotty_trios.isdisjoint(plain_trios):
                ans+=1

print(ans)