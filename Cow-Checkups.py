# N=int(input())
# cow=list(map(int,input().split()))
# need=list(map(int,input().split()))

# start=[1 if cow[i]==need[i] else 0 for i in range(N)]
# pref=[0]*(N+1)
# for i in range(N):
#     pref[i+1]=pref[i]+start[i]


# #[s][i] is num match cow[k] is need[s-k] for k in [0, i)
# diag=[[0]*(N + 1) for _ in range(2*N-1)]

# for s in range(2*N-1):
#     for i in range(N):
#         diag[s][i+1]=diag[s][i]
#         j=s-i
#         if 0<=j<N and cow[i]==need[j]:
#             diag[s][i+1]+=1

# ans=[0]*(N+1)

# for l in range(N):
#     for r in range(l,N):
#         out=pref[l]+(pref[N]-pref[r+1])
#         s=l+r
#         ins=diag[s][r+1]-diag[s][l]
#         total=out+ins
#         ans[total]+=1

# for x in ans:
#     print(x)


import sys
input = sys.stdin.readline

N = int(input())
cow = list(map(int, input().split()))
need = list(map(int, input().split()))

# prefix matches
pref = [0] * (N + 1)
for i in range(N):
    pref[i + 1] = pref[i] + (cow[i] == need[i])

# cache for diagonals
diag_cache = {}

def get_diag(s):
    if s in diag_cache:
        return diag_cache[s]

    d = [0] * (N + 1)
    for i in range(N):
        d[i + 1] = d[i]
        j = s - i
        if 0 <= j < N and cow[i] == need[j]:
            d[i + 1] += 1

    diag_cache[s] = d
    return d

ans = [0] * (N + 1)

# EXACT same (l, r) logic as original
for l in range(N):
    for r in range(l, N):
        out = pref[l] + (pref[N] - pref[r + 1])
        s = l + r
        d = get_diag(s)
        ins = d[r + 1] - d[l]
        ans[out + ins] += 1

for x in ans:
    print(x)
