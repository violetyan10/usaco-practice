# N,Q=map(int,input().split())
# close=list(map(int,input().split()))
# visit=list(map(int,input().split()))
# for i in range(Q):
#     V,S=map(int,input().split())
#     num=0
#     for i in range(N):
#         if visit[i]+S<close[i]:
#             num+=1
#     if num>=V:
#         print("YES")
#     else:
#         print("NO")

N,Q=map(int,input().split())
close=list(map(int,input().split()))
visit=list(map(int,input().split()))

difference=[]
for i in range(N):
    difference.append(close[i] - visit[i])
difference=sorted(difference)

def count_greater(arr,x):
    left,right=0,len(arr)
    while left<right:
        mid=(left+right)//2
        if arr[mid]<=x:
            left=mid+1
        else:
            right=mid
    return len(arr)-left

for _ in range(Q):
    V,S=map(int,input().split())
    if count_greater(difference, S)>=V:
        print("YES")
    else:
        print("NO")
