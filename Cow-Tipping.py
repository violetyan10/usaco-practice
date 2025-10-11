inp = open("cowtip.in", "r").readlines()

N = int(inp[0])


tipped=[]
for _ in range(N):
    tipped.append(list(map(int,[*inp[_ + 1].strip()])))


count=0
for row in range(N-1,-1,-1): #rows
    for col in range(N-1,-1,-1): #columns
        if tipped[row][col]==1:
            count+=1
            for i in range(row+1):
                for j in range(col+1):
                    if tipped[i][j]==1:
                        tipped[i][j]=0
                    else:
                        tipped[i][j]=1

with open("cowtip.out", "w") as out:
    out.write(str(count))