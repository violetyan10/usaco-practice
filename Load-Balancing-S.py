import sys

sys.stdin = open("balancing.in", "r")
sys.stdout = open("balancing.out", "w")

N=int(sys.stdin.readline())
cows=[]
for _ in range(N):
    cows.append(tuple(map(int,sys.stdin.readline().split())))

cows=sorted(cows,key=lambda x:x[1])

minimum=100000000000000000000000000000
As=set()
Bs=set()
for cow in cows:
    x,y=cow
    As.add(x+1)
    Bs.add(y+1)
As=sorted([*As])
Bs=sorted([*Bs])
#7,3
# print(cows)
for a in As:
    topL=0
    topR=0
    botL=0
    botR=0
    for cow in cows:
        x,y=cow
        if x>a:
            topR+=1
        else:
            topL+=1
        # if a==6:
        #     print(x)
            # print(x>a)
        # if a==6:
        #     print(topL, topR, botL, botR)

#faster cause i dont have a triple for loop yay
#B axis is horizontal like this thingy -
    for i in range(len(cows)):      #goes through the range of cows
        b=cows[i][1]+1        #uhhh checks a position of b right above of the cow we're on rn
        j=i             #to like not change the i cause thats kinda bad ngl
        while j<len(cows) and cows[j][1]==b-1:      #continues as long as j (cow we're on) is still within range and if the cow we're on's y-coor is right above the b-axis
            if cows[j][0]>a:    #checks if the x coordinate puts it on the right bottom quadrant
                botR+=1 
                topR-=1 
            else:
                botL+=1
                topL-=1 
            j+=1  #continues moving on to the cow right after since we sorted it by y values. continue while loop to check for the edge case of multiple cows having the same y-coor val
        i=j-1   #bc when it exits the while loop, the j value is one too high (on a value that doesn't work and is right above one that works)

        M=max(topL,topR,botL,botR)
        if M<minimum:
            minimum=M
print(minimum)


#fully understand
#how and why of the while loop
#why j less than lens
    #checks if j (i) out of range 
#why i=j-1
#why faster