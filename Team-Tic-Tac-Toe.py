import sys

sys.stdin = open("tttt.in", "r")
sys.stdout = open("tttt.out", "w")

board=[]
for _ in range(3):
    board.append(list(sys.stdin.readline().strip()))

#check individual wins
individual=set()
two_cows=set()

#checks given a list if its an individual win or two cow win
def check_win(line):
    line_set=set(line)
    if len(line_set)==1:
        individual.add(line_set.pop())
    elif len(line_set)==2:
        a,b=sorted(line_set)
        two_cows.add((a,b))

#check rows
for row in board:
    check_win(row)
#check columns
for column in range(3):
    col_list=[]
    for row in range(3):
        col_list.append(board[row][column])
    check_win(col_list)
#check \
first_diag=[]
for i in range(3):
    first_diag.append(board[i][i])
check_win(first_diag)
#check /
second_diag=[]
for i in range(3):
    second_diag.append(board[i][2-i])
check_win(second_diag)

print(len(individual))
print(len(two_cows))