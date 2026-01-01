# N,U=map(int,input().split())
# paint=[]
# for _ in range(N):
#     paint.append(list(input()))
# updates=[]
# for _ in range(U):
#     updates.append(list(map(int,input().split())))

# #2,2.  3,1.  4,0
# change=0
# for row in range(N//2):
#     for col in range(N//2):
#         points=[(row,col),(row,N-1-col),(N-1-row,N-1-col),(N-1-row,col)]
#         ans=sum(paint[point[0]][point[1]]=="#" for point in points )
#         if ans==1 or ans==3:
#             change+=1
#         if ans==2:
#             change+=2
# print(change)
# for i in range(U):
#     r,c=updates[i]
#     if paint[r-1][c-1]=="#":
#         paint[r-1][c-1]="."
#     else:
#         paint[r-1][c-1]="#"
#     change=0
#     for row in range(N//2):
#         for col in range(N//2):
#             points=[(row,col),(row,N-1-col),(N-1-row,N-1-col),(N-1-row,col)]
#             ans=sum(paint[point[0]][point[1]]=="#" for point in points )
#             if ans==1 or ans==3:
#                 change+=1
#             if ans==2:
#                 change+=2
#     print(change)

N,U=map(int,input().split())
paint=[]
for _ in range(N):
    paint.append(list(input()))
updates=[]
for _ in range(U):
    updates.append(list(map(int,input().split())))

#2,2.  3,1.  4,0
change=0
for row in range(N//2):
    for col in range(N//2):
        points=[(row,col),(row,N-1-col),(N-1-row,N-1-col),(N-1-row,col)]
        ans=sum(paint[point[0]][point[1]]=="#" for point in points )
        if ans==1 or ans==3:
            change+=1
        if ans==2:
            change+=2
print(change)
for i in range(U):
    r,c=updates[i]
    r-=1
    c-=1
    points=[(r,c),(r,N-1-c),(N-1-r,N-1-c),(N-1-r,c)]
    ans1=sum(paint[point[0]][point[1]]=="#" for point in points)
    change-=min(ans1,4-ans1)
    if paint[r][c]=="#":
        paint[r][c]="."
    else:
        paint[r][c]="#"
    points=[(r,c),(r,N-1-c),(N-1-r,N-1-c),(N-1-r,c)]
    ans2=sum(paint[point[0]][point[1]]=="#" for point in points)
    change+=min(ans2,4-ans2)
    print(change)
    
    