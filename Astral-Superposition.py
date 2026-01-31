T=int(input())
for _ in range(T):
    N,A,B=map(int,input().split())
    sky=[]
    for i in range(N):
        sky.append(input().strip())
    stars=[[False]*N for _ in range(N)]
    # stars=0
    keep=True
    # grayed=[]
    for i in range(N):
        for j in range(N):
            star=sky[i][j]
            if star=="B":
                if i-B<0 or j-A<0:
                    keep=False
                stars[i][j]=True
                stars[i-B][j-A]=True
                # nextI=i+B
                # nextJ=j+A
                # stars+=1
                # if nextI>N and nextJ>N:
                #     if sky[nextI][nextJ]=="W":
                #         keep=False
                #         break
                #     # stars+=1
                #     grayed.append([nextI,nextJ])
            # elif star=="G":
            #     if [i,j] not in grayed:
            #         nextI=i+B
            #         nextJ=j+A
            #         stars+=1
            #         if nextI>N and nextJ>N:
            #             # if sky[nextI][nextJ]=="W":
            #             #     keep=False
            #             #     break
            #             # stars+=1
            #             grayed.append([nextI,nextJ])
            #     #gray star on first and moves
    for i in range(N):
        for j in range(N):
            star=sky[i][j]
            if star=="W":
                if stars[i][j]:
                    keep=False
            elif star=="G":
                if stars[i][j]:
                    continue
                if i>=B and j>=A and stars[i-B][j-A]:
                    continue
                stars[i][j]=True
    if not keep:
        print(-1)
        continue
    print(sum(sum(row) for row in stars))
