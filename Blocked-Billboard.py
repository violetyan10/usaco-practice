import sys

sys.stdin = open("billboard.in", "r")
sys.stdout = open("billboard.out", "w")

x1,y1,x2,y2= map(int, sys.stdin.readline().split())
x3,y3,x4,y4,= map(int, sys.stdin.readline().split())
x5,y5,x6,y6,= map(int, sys.stdin.readline().split())
total=set()
for i in range(x1,x2):
    for j in range(y1,y2):
        total.add((i,j))
for i in range(x3,x4):
    for j in range(y3,y4):
        total.add((i,j))
for i in range(x5,x6):
    for j in range(y5,y6):
        total.discard((i,j))
print(len(total))