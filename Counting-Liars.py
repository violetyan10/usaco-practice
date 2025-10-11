N=int(input())
info=[]
for _ in range(N):
    temp=input().split()[::-1]
    temp[0]=int(temp[0])
    info.append(temp)
info=sorted(info)
minAns=1002
for pi in info: #bessies location
    besLoc=int(pi[0])
    curMin=0
    for check in info: #check how many liars
        dir=check[1] #G or L
        if dir=="G":
            if besLoc<check[0]:
                curMin+=1
        else:
            if besLoc>check[0]:
                curMin+=1
    if curMin<minAns:
        minAns=curMin
print(minAns)