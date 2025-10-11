import sys

sys.stdin = open("balancing.in", "r")
sys.stdout = open("balancing.out", "w")

N,B=list(map(int,sys.stdin.readline().split()))
cows=[] #(x,y)
for _ in range(N):
    cows.append(tuple(map(int,sys.stdin.readline().split())))

minimum=100000000000000000000000000000
As=set()
Bs=set()
for cow in cows:
    x,y=cow
    As.add(x+1)
    Bs.add(y+1)
As=sorted([*As])
Bs=sorted([*Bs])
#7,3
for a in As:
    # print("a: "+str(a))
    for b in Bs:
        # print("b: "+str(b))
        topL=0
        topR=0
        botL=0
        botR=0
        for cow1 in cows:
            x2,y2=cow1
            if x2<a and y2>b:
                topL+=1
            elif x2>a and y2>b:
                topR+=1
            elif x2>a and y2<b:
                botR+=1
            else:
                botL+=1
        M=max(topL,topR,botL,botR)
        # print(M)
        if M<minimum:
            minimum=M
print(minimum)
