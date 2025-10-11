import sys

sys.stdin = open("race.in", "r")
sys.stdout = open("race.out", "w")

K,N = map(int, sys.stdin.readline().split())
Xs=[int(sys.stdin.readline().strip()) for _ in range(N)]
 
for X in Xs:
    time=0
    cur_speed=1
    #left hand and right hand side
    left_side=0
    right_side=0
    while True:
        left_side+=cur_speed
        time+=1
        if left_side+right_side>=K:
            print(time)
            break
        if cur_speed>=X:
            right_side+=cur_speed
            time+=1
            if left_side+right_side>=K:
                print(time)
                break
        cur_speed+=1