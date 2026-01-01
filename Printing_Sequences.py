def is_repeating_list(lst):
    n = len(lst)
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            if lst[:i] * (n // i) == lst:
                return True
    return False


def min_prints(seq,K):
    n = len(seq)
    INF = K + 1
    dp = [[INF] * (n + 1) for _ in range(n)]

    for i in range(n):
        dp[i][i + 1] = 1

    for length in range(2, n + 1):
        for l in range(n - length + 1):
            r = l + length
            segment = seq[l:r]

            # repetition check (NO BREAK)
            for k in range(1, length):
                if length % k == 0:
                    if segment[:k] * (length // k) == segment:
                        dp[l][r] = min(dp[l][r], dp[l][l + k])

            # split check
            for m in range(l + 1, r):
                cost = dp[l][m] + dp[m][r]
                if cost < dp[l][r]:
                    dp[l][r] = cost

            # cap value
            if dp[l][r] > K:
                dp[l][r] = INF

    return dp[0][n]
    # n = len(seq)
    # INF = K + 1
    # dp = [[INF] * (n + 1) for _ in range(n)]

    # for i in range(n):
    #     dp[i][i + 1] = 1

    # for length in range(2, n + 1):
    #     for l in range(n - length + 1):
    #         r = l + length
    #         segment = seq[l:r]

    #         # repetition check
    #         for k in range(1, length):
    #             if length % k == 0:
    #                 if segment[:k] * (length // k) == segment:
    #                     dp[l][r] = dp[l][l + k]
    #                     break

    #         if dp[l][r] <= K:
    #             continue

    #         # split check
    #         for m in range(l + 1, r):
    #             cost = dp[l][m] + dp[m][r]
    #             if cost < dp[l][r]:
    #                 dp[l][r] = cost
    #             if dp[l][r] <= K:
    #                 break

    # return dp[0][n]



T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    output = list(map(int, input().split()))

    if K == 1:
        print("YES")
        continue

    if K == 2:
        first = output[0]
        second = 2 if first == 1 else 1
        index = 1
        valid = True

        for x in output:
            if index == 1 and x == first:
                continue
            elif index == 1 and x == second:
                index = -1
            elif index == -1 and x == second:
                continue
            else:
                valid = False
                break

        if valid or is_repeating_list(output):
            print("YES")
        else:
            print("NO")
        continue

    if min_prints(output,3) <= 3:
        print("YES")
    else:
        print("NO")
