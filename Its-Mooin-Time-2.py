N=int(input())
contest=list(map(int,input().split()))
temp=set(contest)
temp=sorted(temp)

pos={}
for i in range(N):
    v=contest[i]
    if v in pos:
        pos[v].append(i)
    else:
        pos[v]=[i]

second_last={}
for v in pos:
    if len(pos[v])>=2:
        second_last[pos[v][-2]]=v

seen=set()
ans=0

for i in range(N):
    seen.add(contest[i])

    if i in second_last:
        num=second_last[i]
        count=len(seen)
        if num in seen:
            count-=1
        ans+=count

print(ans)
