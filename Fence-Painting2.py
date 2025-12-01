import sys

sys.stdin = open("paint.in", "r")
sys.stdout = open("paint.out", "w")

a,b=list(map(int,sys.stdin.readline().split()))
c,d=list(map(int,sys.stdin.readline().split()))
start=0
end=0


if a>c:
    start=c
else:
    start=a

if b>d:
    end=b
else:
    end=d

if b<c or d<a:
    print((b-a)+(d-c))
else:
    print(end-start)