import sys

sys.stdin = open("shuffle.in", "r")
sys.stdout = open("shuffle.out", "w")

N = int(sys.stdin.readline())
order= list(map(int, sys.stdin.readline().split()))
ID=list(map(int, sys.stdin.readline().split()))

#for o in order: why dont work here but work over
    #o-=1

for _ in range(3):
    ID_order=[0]*N
    for i in range(N):
        ID_order[i]=ID[order[i]-1] #here
    ID=ID_order

for cow in ID:
    print(cow)