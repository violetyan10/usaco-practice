# N,T=map(int,input().split())
# count=0
# #delivery={}
# for _ in range(N):
#     day,num=(map(int,input().split()))
#     count+=num
#     #delivery[day]=num
# if count>T:
#     print(T)
# else:
#     print(count)
N,T=map(int,input().split())

delivery={}
for _ in range(N):
    day,num=(map(int,input().split()))
    delivery[day]=num
delivery[T+1]=0
count=0
prev_day=0
leftover=0
for day,num in delivery.items():
    count+=num #2
    left=leftover-(day-prev_day)   #-2
    if left<0:
        leftover=num
        # if leftover>0:
        #     store=leftover+left
        #     if store<0:
        #         leftover=0
        #     else:
        #         leftover=store
    else:
        leftover=left+num
    #print(leftover)
    prev_day=day

ans=count-leftover
if ans>T:
    print(T)
else:
    print(ans)