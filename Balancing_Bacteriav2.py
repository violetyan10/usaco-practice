N=int(input())
bacteria=list(map(int,input().split()))

# ans=0 #1
# effects=0 #2
# diff=0

# for i in range(N):
#     grass=bacteria[i]
#     cur=grass+effects
    
#     ans+=abs(cur)
#     if cur<0:
#         effects+=cur*2+i
#     else:
#         effects+=-cur-i-1

ans=0

for i in range(N):
    grass=bacteria[i]
    for j in range(i,N):
        bacteria[j]+=-grass*(j-i+1)
    ans+=abs(grass)
print(ans)