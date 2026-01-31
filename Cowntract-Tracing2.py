N=int(input())
infected=input().strip()
count=0
chains=[]
for i in range(N):
    if infected[i]=="1":
        count+=1
    else:
        if count:
            chains.append(count)
        count=0
if count:
    chains.append(count)

ans=N
for length in range(1,N+1,2):
    og=0
    valid=True
    for i,chunk in enumerate(chains):
        if (i==0 and infected[0]=="1") or (i==len(chains)-1 and infected[-1]=="1"):
            if length>chunk*2-1:
                valid=False
                break
        else:
            if length>chunk:
                valid=False
                break
        og+=(chunk+length-1)//length
    if not valid:
        break
    ans=min(ans,og)
print(ans)