N,M=list(map(int,input().split()))
beats=[[False for _ in range(N)]for __ in range(N)]
for i in range(N):
    line=input()
    for j in range(len(line)):
        if line[j]=="W":
            beats[i][j]=True
        elif line[j]=="L":
            beats[j][i]=True
#print(beats)

elsie=[]
for k in range(M):
    elsie.append(tuple(map(int,input().split())))
#print(elsie)


for x,y in elsie:
    x-=1
    y-=1
    ans=0
    right=0
    for r in beats:
        if r[x] and r[y]:
            right+=1
    for l in beats:
        if l[x] and l[y]:
            ans+=N
        else:
            ans+=right
    print(ans)