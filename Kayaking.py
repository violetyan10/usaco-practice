N=int(input())
w=list(map(int, input().split()))
min_weight=100000000000000000000000000000000000000000000000000000
ppl=2*N
for i in range(ppl):
    for j in range(i+1,ppl): #goes through all possible single kayaker combos
        #got rid of single kayakers
        #find pair with min abs
        remaining=[]
        for k in range(ppl):
            if k!=i and k!=j:
                remaining.append(w[k])
        remaining=sorted(remaining)
        total=0
        for k in range(0,len(remaining),2):
            total+=abs(remaining[k]-remaining[k+1])
        min_weight=min(min_weight, total)

print(min_weight)
