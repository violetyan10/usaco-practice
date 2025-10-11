N=int(input())
flower=list(map(int,input().split()))
res=0

for i in range(N): #start flower
    sum=0
    passed=set()
    for j in range(i,N): #end flower
        sum+=flower[j]
        passed.add(flower[j])
        ranged=j-i+1
        if sum%ranged==0:
            aver=sum/ranged
            if aver in passed:
                res+=1

print(res)