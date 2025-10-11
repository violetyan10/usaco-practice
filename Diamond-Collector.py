import sys

sys.stdin = open("diamond.in", "r")
sys.stdout = open("diamond.out", "w")

N,K = map(int, sys.stdin.readline().split())

diamonds=[]
for _ in range(N):
    diamonds.append(int(sys.stdin.readline()))

diamonds.sort()
max_diamonds=0
cur=0

for i in range(N):
    while diamonds[i]-diamonds[cur]>K:
        cur+=1
    max_diamonds=max(max_diamonds, i-cur+1)
print(max_diamonds)