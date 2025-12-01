N=int(input())
cow_IDs=list(map(int,input().split()))

evens=0
odds=0

for ID in cow_IDs:
    if ID%2==0:
        evens+=1
    else:
        odds+=1

while odds>evens:
    odds-=2
    evens+=1

if evens>odds:
    print(2*odds+1)

elif odds==evens:
    print(2*odds)