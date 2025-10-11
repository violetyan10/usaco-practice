T=int(input())

for _ in range(T):
    N, M=map(int, input().split())
    cards=[list(map(int, input().split())) for _ in range(N)]
    ans=0
    for col in range(M):
        col_vals=sorted(cards[i][col] for i in range(N))
        prefix_sum=0
        for i in range(N):
            ans+=col_vals[i] * i - prefix_sum
            prefix_sum+=col_vals[i]
    print(ans)