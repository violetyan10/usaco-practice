import sys

sys.stdin = open("herding.in", "r")
sys.stdout = open("herding.out", "w")

cows=sorted(list(map(int,sys.stdin.readline().split())))

minimum=0
maximum=0

#all consecutive
if cows[1]-cows[0]==1 and cows[2]-cows[1]==1:
    pass
#one unit gap
elif cows[1]-cows[0]==2 and cows[2]-cows[1]==2:
    minimum=1
    maximum=1
elif cows[1]-cows[0]==2 or cows[2]-cows[1]==2:
    minimum=1
    maximum=max(cows[1]-cows[0], cows[2]-cows[1])-1
#else 2
else:
    minimum=2
    maximum=max(cows[1]-cows[0], cows[2]-cows[1])-1

print(minimum)
print(maximum)