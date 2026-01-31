N,Q=map(int,input().split())
tokens=input().split()

for i in range(0,N,2):
    tokens[i]=tokens[i]=="true"

first_true=float("inf")
last_true=-1

idx=0
while idx<N:
    group_start=idx
    group_value=tokens[group_start]

    while idx+1<N and tokens[idx+1]=="and":
        idx+=2
        group_value &=tokens[idx]

    if group_value:
        first_true=min(first_true,idx)
        last_true=max(last_true,group_start)

    idx+=2

falseLeft=[False]*N
for i in range(2,N,2):
    if tokens[i-1]=="or":
        continue
    falseLeft[i]=falseLeft[i-2] or not tokens[i-2]

falseRight=[False]*N
for i in reversed(range(0,N-1,2)):
    if tokens[i+1]=="or":
        continue
    falseRight[i]=falseRight[i+2] or not tokens[i+2]

results=[]
for _ in range(Q):
    left,right,expected=input().split()
    left=int(left)-1
    right=int(right)-1
    expected=expected=="true"

    evaluated=first_true<left or right<last_true

    if not (falseLeft[left] or falseRight[right]):
        evaluated|=expected

    results.append(expected==evaluated)

print("".join("Y" if x else "N" for x in results))
