N,K=list(map(int,input().split()))
watch=list(map(int,input().split()))
cost=0
prev=0
for day in watch:
    if watch[0]==day:
        cost+=K+1
        continue

    restart=K+1
    cont=(day-watch[prev])
    cost+=min(cont,restart)
    prev+=1
    
print(cost)