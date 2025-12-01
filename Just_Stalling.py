N=int(input())
cow_heights=sorted(list(map(int,input().split())),reverse=True)
barn_heights=list(map(int,input().split()))

total=1
for i,height in enumerate(cow_heights):
    stalls_available=-i
    for stall in barn_heights:
        if stall>=height:
            stalls_available+=1
    total*=stalls_available
print(total)