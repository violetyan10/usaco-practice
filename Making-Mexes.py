# N=int(input())
# array=list(map(int,input().split()))
# for i in range(N+1):
#     ans=0
#     #i is the mex
#     for j in range(i):
#         if j not in array:
#             ans+=1
#     if ans<array.count(i):
#         ans=array.count(i)
#     else:
#         ans+=array.count(i)
#     print(ans)

N = int(input())
array = list(map(int, input().split()))

# Frequency array for values 0..N
freq = [0] * (N + 1)
for x in array:
    if x <= N:
        freq[x] += 1

missing = 0  # count of missing numbers so far

for i in range(N + 1):
    # missing numbers in [0, i)
    if i > 0 and freq[i - 1] == 0:
        missing += 1

    # same logic as your original code
    if missing < freq[i]:
        ans = freq[i]
    else:
        ans = missing# + freq[i]

    print(ans)




