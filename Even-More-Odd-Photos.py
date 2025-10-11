N=int(input())
IDs=list(map(int,input().split()))

even=0
odd=0
for breed in IDs:
    if breed%2==0:
        even+=1
    else:
        odd+=1

groups=0
# flag=True

while even>0 or odd>0:
    if even>=1:
        even-=1
    elif odd>=2:
        odd-=2
    else:
        break
    groups += 1

    if odd>2 or odd==1:
        odd-=1
    elif even>=1 and odd>=1:
        even-=1
        odd-=1
    else:
        break
    groups+=1
    # flag=not flag
    
print(groups)