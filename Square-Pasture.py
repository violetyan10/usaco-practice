import sys

sys.stdin = open("square.in", "r")
sys.stdout = open("square.out", "w")

x1,y1,x2,y2= map(int, sys.stdin.readline().split())
x3,y3,x4,y4= map(int, sys.stdin.readline().split())

min_x=min(x1,x3)
max_x=max(x2,x4)
min_y=min(y1,y3)
max_y=max(y2,y4)

side=max(max_x-min_x,max_y-min_y)

print(side **2)