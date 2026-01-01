N,M=map(int,input().split())
cows=input().strip()
capacity=list(map(int,input().split()))

total=sum(capacity)
cowss=[]

# for i in range(N):
#     cur=i%N
#     nex=(i+1)%N
#     if cows[cur]=cows[nex]:
#         cowss.append(cows[cur])


# for i in range(N):
#     prev=(i-1)%N
#     cur=i%N
#     nex=(i+1)%N
    
#     if cows[prev:nex]=="RL": #substring with prev and cur
#         #nothing ig
#         if cows[nex]=="L":
#             if capacity[nex]<M:
#                 total-=capacity[nex]
#             else:
#                 total-=M
#         if cows[(prev-1)%N]=="R":
#             if capacity[(prev-1)%N]<M:
#                 total-=capacity[(prev-1)%N]      
#             else:
#                 total-=M
# print(total)


for i in range(N):
    prev=(i-1)%N
    cur=i%N
    
    if cows[prev]=="R" and cows[cur]=="L": #substring with prev and cur
        #far back L chain
        sumL=0
        indexL=cur+1
        flagL=True
        while flagL:
            indexL%=N
            if cows[indexL]=="R":
                break
            sumL+=capacity[indexL]
            indexL+=1
        if M>sumL:
            total-=sumL
        else:
            total-=M


        sumR=0
        indexR=prev-1
        flagR=True
        while flagR:
            indexR%=N
            if cows[indexR]=="L":
                break
            sumR+=capacity[indexR]
            indexR-=1
        if M>sumR:
            total-=sumR
        else:
            total-=M
        


print(total)