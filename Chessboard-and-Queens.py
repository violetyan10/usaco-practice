board=[]
for _ in range(8):
    board.append([True]*8) #true indicates spot is free :P

for i in range(8):
    row=input()
    for j in range(8):
        if row[j]=="*":
          board[i][j]=False

sides=8

def perms():
    result=[]
    cur_perm=[]
    def make_list(pos):
        if pos==sides:
            result.append(cur_perm[:])
        else:
            for i in range(sides):
                if i not in cur_perm:
                    cur_perm.append(i)
                    make_list(pos+1)
                    cur_perm.pop()
    make_list(0)
    return result

works=0
perms=perms()
for queen_list in perms:
    flag=True
    #restricted?
    for square in range(sides): #i just as confused as u
        if not board[queen_list[square]][square]:
            flag = False
            break
    #ugh diagonals
    #\
    free=[True]*(15)
    for i in range(sides): #i is row num
        if not free[queen_list[i]-i+sides-1]:
            flag=False
            break
        free[queen_list[i]-i+sides-1]=False
    #/
    free=[True]*(15)
    for j in range(sides): #j is row num
        if not free[j+queen_list[j]]:
            flag=False
            break
        free[j+queen_list[j]] = False
    if flag:
        works+=1

print(works)