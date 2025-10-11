inp = open("gymnastics.in", "r").readlines()

K,N = map(int, inp[0].split())

ranks=[]
for _ in range(K):
    ranks.append(list(map(int,inp[_ + 1].strip().split(" "))))

pairs=0

for i in range(1,N+1): #first cow
    for j in range(i+1,N+1): #second cow
        consistent=True
        if ranks[0].index(i)>ranks[0].index(j):
            for rank in ranks:
                if rank.index(i)<rank.index(j):
                    consistent=False
                    break
            if consistent:
                pairs+=1
        else:
            for rank in ranks:
                if rank.index(i)>rank.index(j):
                    consistent=False
                    break
            if consistent:
                pairs+=1
with open("gymnastics.out", "w") as out:
    out.write(str(pairs) + "\n")