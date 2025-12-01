def win(first_list,second_list):
    first_win=0
    second_win=0
    for a in first_list:
        for b in second_list:
            if a>b:
                first_win+=1
            if b>a:
                second_win+=1
    return first_win,second_win


T=int(input())
for _ in range(T):
    temp=list(map(int,input().split()))
    A=temp[:4]
    B=temp[4:]

    A_win,B_win=win(A,B)
    
    
    if A_win==B_win:
        print("no")
        continue
    
    flag=False

    for first in range(1,11):
        if flag:
            break
        for second in range(1,11):
            if flag:
                break
            for third in range(1,11):
                if flag:
                    break
                for forth in range(1,11):
                    C=[first,second,third,forth]

                    if A_win>B_win:
                        #a beat b so b beat c and c beat a
                        win_B,win_C=win(B,C)
                        if win_B<=win_C:
                            continue
                        win_A,win_C=win(A,C)
                        if win_A>=win_C:
                            continue
                        flag=True
                        break
                    else:
                        #b beats a so a beats c and c beats b
                        win_A,win_C=win(A,C)
                        if win_A<=win_C:
                            continue
                        win_B,win_C=win(B,C)
                        if win_B>=win_C:
                            continue
                        flag=True
                        break
    if flag:
        print("yes")
    else:
        print("no") 


