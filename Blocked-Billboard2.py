import sys

sys.stdin = open("billboard.in", "r")
sys.stdout = open("billboard.out", "w")

x1,y1,x2,y2= map(int, sys.stdin.readline().split()) #lawn
x3,y3,x4,y4= map(int, sys.stdin.readline().split()) #cow

lawn=(x2-x1)*(y2-y1)

if (x3<=x1 and x4>=x2) and (y3<=y1 and y4>=y2):
    print(0)
elif x3<=x1 and x4>=x2:
    #x covered
    if y3<=y1 and y4<y2:
        print((x2-x1)*(y2-y4))   #top
    elif y3>y1 and y4>=y2:
        print((x2-x1)*(y3-y1))    #bottom
    else:
        print(lawn)
        #print(abs((x2-x1)*((y3-y1)+(y2-y4))))   #both
elif y3<=y1 and y4>=y2:
    #y covered
    if x3<=x1 and x4<x2:
        print((y2-y1)*(x2-x4))    #right
    elif x3>x1 and x4>=x2:
        print((y2-y1)*(x3-x1))   #left
    else:
        print(lawn)
        #print((y2-y1)*((x3-x1)+(x2-x4)))  #both
else:
    print(lawn)