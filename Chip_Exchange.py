def can(x, A, B, cA, cB, fA):
    final1 = A + cA * ((B + x) // cB)
    final2 = A + 1 + cA * ((B + x - 1) // cB) if x != 0 else final1
    return min(final1, final2) >= fA



T = int(input())
for _ in range(T):
    A, B, exchA, exchB, end = map(int, input().split())

    if A >= end:
        print(0)
        continue

    lo,hi=0,10**18
    ans=hi
    while lo<=hi:
        mid=(lo+hi)//2
        if can(mid,A,B,exchA,exchB,end):
            ans=mid
            hi=mid-1
        else:
            lo=mid+1

    print(ans)
