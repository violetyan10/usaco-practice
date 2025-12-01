N=int(input())
initial=list(map(int,input().split()))
goal=list(map(int,input().split()))

index=0

moves=0

for i in range(N):
    if goal[i]==initial[i]:
        continue
    index=initial.index(goal[i])
    initial.insert(i,goal[i])
    initial.pop(index+1)
    moves+=1
    if initial==goal:
        break
    index+=1

print(moves)