T=int(input())

for _ in range(T):
    N,K = map(int, input().split())
    grid=[input().strip() for _ in range(N)]

    #dp[r][c][d][t]
    #reach (r,c)
    #0 r 1 d

    stats=[[[[0]*(K+1) for _ in range(2)]
           for _ in range(N)] for _ in range(N)]

    if N>1:
        if grid[0][1]=='.':
            stats[0][1][0][0]=1
        if grid[1][0]=='.':
            stats[1][0][1][0]=1

    for r in range(N):
        for c in range(N):
            if grid[r][c]=='H':
                continue

            for d in range(2):
                for t in range(K + 1):
                    ways=stats[r][c][d][t]
                    if not ways:
                        continue

                    #r
                    if c+1<N and grid[r][c+1]=='.':
                        nt=t+(d!=0)
                        if nt<=K:
                            stats[r][c+1][0][nt]+=ways

                    #d
                    if r+1<N and grid[r+1][c]=='.':
                        nt=t+(d!=1)
                        if nt<=K:
                            stats[r+1][c][1][nt]+=ways

    print(sum(stats[N-1][N-1][d][t]
                 for d in range(2)
                 for t in range(K+1)))

