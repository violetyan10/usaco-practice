def solve(N,K,Q,updates):
    grid=[[0]*N for _ in range(N)]
    prefix_sum=[[0]*N for _ in range(N)]
    
    def update_prefix_sum(r,c,delta):
        for i in range(r,N):
            for j in range(c,N):
                prefix_sum[i][j]+=delta

    def get_max_attractiveness():
        max_attractiveness=0
        for r in range(N-K+1):
            for c in range(N-K+1):
                sum_kxk=(prefix_sum[r+K- 1][c+K- 1]
                           -(prefix_sum[r-1][c+K- 1] if r>0 else 0)
                           -(prefix_sum[r+K-1][c-1] if c>0 else 0)
                           +(prefix_sum[r-1][c-1] if r>0 and c>0 else 0))
                max_attractiveness=max(max_attractiveness,sum_kxk)
        return max_attractiveness
    
    results=[]
    for r,c,v in updates:
        r-=1
        c-=1
        
        old_value=grid[r][c]
        delta=v-old_value
        
        grid[r][c]=v
        
        update_prefix_sum(r,c,delta)
        
        max_attractiveness=get_max_attractiveness()
        results.append(max_attractiveness)
    
    return results

N,K=map(int,input().split())
Q=int(input())
updates=[tuple(map(int,input().split())) for _ in range(Q)]

results=solve(N,K,Q,updates)

for result in results:
    print(result)
