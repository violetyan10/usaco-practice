import sys

sys.stdin = open("circlecross.in", "r")
sys.stdout = open("circlecross.out", "w")

crossing=sys.stdin.readline().strip()

positions={}
for idx,cow in enumerate(crossing):
    if cow in positions:
        positions[cow].append(idx)   
    else:
        positions[cow]=[idx]

cross=0

for i in range(26):
    for j in range(i+1, 26):
        cow1=chr(ord('A')+i)
        cow2=chr(ord('A')+j)

        a1,a2=positions[cow1]
        b1,b2=positions[cow2]

        if (a1<b1<a2)!=(a1<b2<a2):
            cross += 1

print(cross)