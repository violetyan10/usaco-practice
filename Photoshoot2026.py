N,K=map(int,input().split())
Q=int(input())
# updates=[]
# for _ in range(Q):
#     updates.append(list(map(int,input().split())))
board=[[0 for i in range(N)] for j in range(N)]
sums=[[0 for i in range(N)] for j in range(N)] #sum of kxk square with top at r,c
maxval=0
for i in range(Q):
    r,c,v=list(map(int,input().split()))
    r-=1
    c-=1
    # if i==0:
    #     print(v)
    #     board[r][c]=v
    #     continue
    diff=v-board[r][c]
    board[r][c]=v
    for a in range(max(r-K+1,0),min(r,N-K)+1):
        for b in range(max(c-K+1,0),min(c,N-K)+1):
            sums[a][b]+=diff
            maxval=max(maxval,sums[a][b])
    
    print(maxval)