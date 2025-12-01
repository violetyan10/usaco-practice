# T=int(input())
# for _ in range(T):
#     N=int(input())
#     H=list(map(int, input().split()))

#     lowest=min(H)
#     flag=False
#     for level in range(lowest,-1,-1):
#         copy=H[:]
#         bags=0
#         work=True
#         for i in range(N-1):
#             if copy[i]<level:
#                 work=False
#                 break
#             hunger=copy[i]-level
#             copy[i]-=hunger
#             copy[i+1]-=hunger
#             bags+=2*hunger
#         if work and copy[-1] == level:
#             flag=True
#             print(bags)
#             break
#     if not flag:
#         print(-1)


# T=int(input())
# for _ in range(T):
#     N=int(input())
#     H=list(map(int, input().split()))

#     #lowest=min(H)
#     highest=max(H)
#     flag=False
#     for level in range(highest,-1,-1):
#         #copy=H[:]
#         copy=H.copy()
#         bags=0
#         work=True
#         for i in range(N-1):
#             if copy[i]<level:
#                 work=False
#                 break
#             hunger=copy[i]-level
#             copy[i]-=hunger
#             copy[i+1]-=hunger
#             bags+=2*hunger
#         if work and copy[-1] == level:
#             flag=True
#             print(bags)
#             break
#     if not flag:
#         print(-1)

T=int(input())

for _ in range(T):
    N=int(input())
    H=list(map(int,input().split()))

    #check if first index is smaller than or eual to next index
    if N==1:
        print(0)
        continue
    if H[0]>H[1]:
        print(-1)
        continue
    if H[-1]>H[-2]:
        print(-1)
        continue




    #first one
    grass=0
    for index in range(1,N-1):
        prev_i=index-1
        next_i=index+1

        if H[index]>H[prev_i]:
            diff=H[index]-H[prev_i]
            grass+=diff*2
            H[index]=H[prev_i]
            H[next_i]-=diff

        #pairs
        #cur great prev
    
    for index in range(N-2,0,-1):
        prev_i=index+1
        next_i=index-1

        if H[index]>H[prev_i]:
            diff=H[index]-H[prev_i]
            grass+=diff*2
            H[index]=H[prev_i]
            H[next_i]-=diff
    
    fleg=True
    for j in H:
        if j<0:
            print(-1)
            fleg=False
            break
    if not fleg:
        continue
    else:
        print(grass)
