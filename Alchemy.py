N=int(input())
metal_units=list(map(int,input().split()))
metal_units.insert(0,0)
K=int(input())
recipies=[]
for _ in range(K):
    recipies.append(list(map(int,input().split())))

recipies=sorted(recipies)

elements_need=[[]for _ in range(N+1)]
for recipie in recipies:
    index=recipie[0]
    temp=[]
    for i in range(recipie[1]):
        temp.append(recipie[2+i])
    elements_need[index]=temp
#print(elements_need)



#base is when have thy metals
def create_metal(metal):
    if metal_units[metal]>0:
        metal_units[metal]-=1
        return True
    element=elements_need[metal]
    if len(element)==0:
        return False
    for i in range(len(element)):
        if not create_metal(element[i]):
            return False
    return True

ans=0
while create_metal(N):
    ans+=1

print(ans)