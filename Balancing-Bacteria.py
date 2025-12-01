N=int(input())
level=list(map(int,input().split()))
    
ans=0
infl=0 #total influence (bact) on cur 
net=0 #net num sprays active
    
for i in range(N):
    infl+=net
    level[i]+=infl
        
    cur=-level[i]
    ans+=abs(cur)
    net+=cur
    infl+=cur
    
print(ans)