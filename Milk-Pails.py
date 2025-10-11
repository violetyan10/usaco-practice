import sys

sys.stdin = open("pails.in", "r")
sys.stdout = open("pails.out", "w")

X,Y,M = map(int, sys.stdin.readline().split())

max_Y=int(M/Y) #maximum amount of Y M can have inside

max_milk=0

for i in range(max_Y+1): #iterates through 0 up to the max amount of Y M can have
    #have i Y pails
    cur_max=Y*i
    max_X=int((M-cur_max)/X)
    cur_max+=max_X*X
    if cur_max>max_milk:
        max_milk=cur_max
print(max_milk)