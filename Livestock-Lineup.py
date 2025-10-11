import sys

sys.stdin = open("lineup.in", "r")
sys.stdout = open("lineup.out", "w")

N = int(sys.stdin.readline())
constraints=[(sys.stdin.readline().strip().split()) for _ in range(N)]

cows= sorted(["Bessie", "Buttercup", "Belinda", "Beatrice", "Bella", "Blue", "Betsy", "Sue"])
dict={c:[] for c in cows} #  **

for con in constraints:
    cur=con[0]
    next=con[-1]
    dict[cur].append(next)
    dict[next].append(cur)


order=[]
seen=set()

for cow in cows:
    if cow in seen:
        continue
    length=len(dict[cow])
    if length==0:
        order.append(cow)
    elif length==1:
        cur=cow
        next=dict[cow][0]
        while True:
            if len(dict[cur])==1 and cur!=cow:
                seen.add(cur)
                order.append(cur)
                break
            order.append(cur)
            seen.add(cur)
            cur=next
            if dict[cur][0] in seen and len(dict[cur])==1:
                order.append(cur)
                seen.add(cur)
                break
            elif dict[cur][0] in seen:
                next=dict[cur][1]
            else:
                next=dict[cur][0]
            
            
for ord in order:
    print(ord)
            



