import sys

sys.stdin = open("factory.in", "r")
sys.stdout = open("factory.out", "w")

N=int(sys.stdin.readline())

reached=[[] for _ in range(N+1)]

for _ in range(N-1):
    a,b = map(int, sys.stdin.readline().split())
    reached[b].append(a)

def check(node,seen):
    seen[node]=True
    for next in reached[node]:
        if not seen[next]:
            check(next,seen)

for i in range(1, N+1):
    seen=[False]*(N+1)
    check(i,seen)
    if all(seen[1:]):
        print(i)
        break
else:
    print(-1)