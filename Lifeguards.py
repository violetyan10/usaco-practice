import sys

sys.stdin = open("lifeguards.in", "r")
sys.stdout = open("lifeguards.out", "w")

N=(int(sys.stdin.readline()))

shifts=[]
for _ in range(N):
    shifts.append((list(map(int,sys.stdin.readline().split()))))

time=[0 for _ in range(1001)]

for shift in shifts:
    x,y=shift
    for i in range(x,y):
        time[i]+=1

ans=0
for fire in shifts:
    cur_max=0
    x0,y0=fire
    for j in range(x0,y0):
        time[j]-=1
    for t in time:
        if t>0:
            cur_max+=1
    for j in range(x0,y0):
        time[j]+=1
    ans=max(ans,cur_max)
print(ans)