import sys

sys.stdin = open("bcs.in", "r")
sys.stdout = open("bcs.out", "w")

N,K = map(int, sys.stdin.readline().split())
figure=[]
pieces=[]
for _ in range(N):
    figure.append(sys.stdin.readline())
for _ in range(K):
    board=[]
    for _ in range(N):
        board.append(sys.stdin.readline())
    pieces.append(board)

target_pos=[]

for i in range(N):
    for j in range(N):
        if figure[i][j]=="#":
            target_pos.append((i,j))

pieces_pos=[]

for piece in pieces:
    pos=[]
    for a in range(N):
        for b in range(N):
            if piece[a][b]=="#":
                pos.append((a,b))
    pieces_pos.append(pos)


for i in range(K):
    for j in range(i+1, K):
        piece1_pos=pieces_pos[i]
        piece2_pos=pieces_pos[j]


        for x1shift in range(-N+1, N):
            for y1shift in range(-N+1, N):
                new_position1=[]
                for (x, y) in piece1_pos:
                    new_x=x+x1shift
                    new_y=y+y1shift
                    if 0<=new_x<N and 0<=new_y<N:
                        new_position1.append((new_x, new_y))

                for x2shift in range(-N + 1, N):
                    for y2shift in range(-N + 1, N):
                        new_position2 = []
                        for (x, y) in piece2_pos:
                            new_x=x+x2shift
                            new_y=y+y2shift
                            if 0<=new_x<N and 0 <=new_y< N:
                                new_position2.append((new_x, new_y))

                        combined=set(new_position1+new_position2)
                        if combined==set(target_pos):
                            print(i+1, j+1)