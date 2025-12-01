N,S=map(int,input().split())
locs=[]
locs.append([-1,-1])
for _ in range(N):
    temp=list(map(int,input().split()))
    locs.append(temp)

direc=1
power=1
breaked=0
pos=S
# print(pos)
seen=set()
#broke=[]

while pos<N+1 and pos>-1:
    if (pos,power,direc) in seen:
        break
    seen.add((pos,power,direc))
    cur=locs[pos]
    #print(cur)
    if cur[0]==1:
        if power>=cur[1]:
            breaked+=1
            cur[0]=-1
    if cur[0]==0:
        power+=cur[1]
        direc*=-1
    pos+=power*direc
# print(seen)
print(breaked)