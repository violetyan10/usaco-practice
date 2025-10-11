import sys

sys.stdin = open("lostcow.in", "r")
sys.stdout = open("lostcow.out", "w")

x,y = map(int, sys.stdin.readline().split())

pos=x
dist=1
dir=1
isLost=True
res=0
while isLost:
    next=x+dir*dist
    if pos<=y<=next or pos>=y>=next:
        res+=abs(y-pos)
        isLost=False
        break
    res+=abs(next-pos)
    pos=next
    dist*=2
    dir*=-1
print(res)