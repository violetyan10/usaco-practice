N,P=map(int,input().split())
posts=[]
cows=[]
for _ in range(P):
    posts.append(tuple(map(int,input().split())))
for _ in range(N):
    cows.append(map(int,input().split()))

fence=[]
for i in range(P):
    cur=posts[i]
    connect=i+1
    if i==P-1:
        connect=0
    connect=posts[connect]
    fence.append(cur)
    if cur[0]==connect[0]:
        #x vals same
        # start=min(cur[1],connect[1])
        # end=max(cur[1],connect[1])
        dirs=1
        if cur[1]>connect[1]:
            dirs*=-1
        for j in range(cur[1]+dirs,connect[1],dirs):
            fence.append((cur[0],j))
    else:
        #y vals same
        dirs=1
        if cur[0]>connect[0]:
            dirs*=-1
        for j in range(cur[0]+dirs,connect[0],dirs):
            fence.append((j,cur[1]))

pos={pt:i for i,pt in enumerate(fence)}
L=len(fence)

for sx,sy,ex,ey in cows:
    s=pos[(sx,sy)]
    e=pos[(ex,ey)]

    d=abs(e-s)
    print(min(d,L-d))
    
# for cow in range(N):
#     startX,startY,endX,endY=cows[cow]
#     startI=fence.index((startX,startY))
#     endI=fence.index((endX,endY))
#     oneW=0
#     anoW=0
#     if startI<endI:
#         oneW=endI-startI
#         anoW=len(fence)-oneW
#     else:
#         oneW=startI-endI
#         anoW=len(fence)-oneW#endI+len(fence)-startI
    
#     print(min(oneW,anoW))
