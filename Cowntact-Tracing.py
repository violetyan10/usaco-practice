import sys

sys.stdin = open("tracing.in", "r")
sys.stdout = open("tracing.out", "w")

N,T= map(int, sys.stdin.readline().split())
infected=sys.stdin.readline().strip()
shakes=[]
for _ in range(T):
    shakes.append(list(map(int, sys.stdin.readline().split())))

shakes=sorted(shakes) #orders it by the time

starter=0
small=12345678908765432
big=-1
work=set()

for i in range(N): #goes through the possibility that cow i is patient 0
    if infected[i]!="1":
        continue
    for j in range(T+1): #goes through all Ks
        #healthy
        infect=["0"]*N
        infect[i]="1" #patient zero

        #min K val
        minimum=[0]*N

        for shake in shakes:
            time, cow1, cow2=shake
            cow1-=1
            cow2-=1
            if infect[cow1]=="1" and infect[cow2]=="0" and minimum[cow1]!=j:
                infect[cow2]="1"
                minimum[cow1]+=1
            elif infect[cow2]=="1" and infect[cow1]=="0" and minimum[cow2]!=j:
                infect[cow1]="1"
                minimum[cow2]+=1
            elif infect[cow2]=="1" and infect[cow1]=="1" and minimum[cow1]!=j and minimum[cow2]!=j:
                minimum[cow1]+=1
                minimum[cow2]+=1
            elif infect[cow2]=="1" and infect[cow1]=="1" and minimum[cow1]!=j:
                minimum[cow1]+=1
            elif infect[cow2]=="1" and infect[cow1]=="1" and minimum[cow2]!=j:
                minimum[cow2]+=1
        flag=True
        for k in range(N):
            if infect[k]!=infected[k]:
                flag=False
        if not flag:
            continue
        small=min(j,small)
        big=max(big,j)
        work.add(i)
starter=len(work)
if big==T:
    big="Infinity"
print(str(starter)+" "+str(small)+" "+str(big))

