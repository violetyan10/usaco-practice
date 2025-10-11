import sys

sys.stdin = open("blist.in", "r")
sys.stdout = open("blist.out", "w")

N = int(sys.stdin.readline())
cows=[]
for _ in range(N):
    cows.append(tuple(map(int, sys.stdin.readline().split())))

bucket_time=[0]*1000 #buckets needed at time

for s,t,b in cows:
    for time in range(s,t):
        bucket_time[time]+=b

print(max(bucket_time))