n,x=list(map(int,input().split()))
values=list(map(int,input().split()))

# for i in range(n):
#     for j in range(i+1,n):
#         num=values[i]+values[j]
#         if num==x:
#             print(i+1,j+1)
#             exit()
if x<=1:
    print("IMPOSSIBLE")
    exit()

seen={}
for i, val in enumerate(values):
    if x-val in seen:
        print(i+1,seen[x-val]+1)
        exit()
    seen[val]=i
print("IMPOSSIBLE")