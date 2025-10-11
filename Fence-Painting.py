import sys

sys.stdin = open("paint.in", "r")
sys.stdout = open("paint.out", "w")

a,b= map(int, sys.stdin.readline().split())
c,d= map(int, sys.stdin.readline().split())
total=set()
for i in range(a,b):
    total.add(i)
for j in range(c,d):
    total.add(j)
print(len(total))