import sys

sys.stdin = open("badmilk.in", "r")
sys.stdout = open("badmilk.out", "w")

N,M,D,S = list(map(int, sys.stdin.readline().split()))

drinking={i:[] for i in range(1,M+1)} #milk dranken by...

for _ in range(D):
    p,m,t=list(map(int, input().split()))
    drinking[m].append([p,t])

sick={i: 0 for i in range(1,N+1)}
for _ in range(S):
    p,t=list(map(int, input().split()))
    sick[p]=t

sick_p=[]
for k,v in sick.items():
    if v!=0:
        sick_p.append(k)

possible=[]
for milk in range(1,M+1):
    flag=True
    for person in sick_p:
        drank_times=[]
        for p, t in drinking[milk]:
            if p==person:
                drank_times.append(t)
        if not drank_times or min(drank_times)>=sick[person]:
            flag=False
            break
    if flag:
        possible.append(milk)

max_contam=0
for milk in possible:
    people_drank = {p for p, t in drinking[milk]}
    max_contam = max(max_contam, len(people_drank))
print(max_contam)