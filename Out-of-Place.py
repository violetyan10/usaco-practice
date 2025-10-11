import sys

sys.stdin = open("outofplace.in", "r")
sys.stdout = open("outofplace.out", "w")

N=int(sys.stdin.readline())
cows=[]
for _ in range(N):
    cows.append(int(input().strip()))

height=sorted(cows)
spot=[]
for i in range(N):
    if cows[i]!=height[i]:
        spot.append(i)
print(len(spot)-1)