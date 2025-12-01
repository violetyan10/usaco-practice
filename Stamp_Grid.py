def rotate_90(stamp):
    # stamp is a list of strings (each same length)
    length=len(stamp)
    rotated=[]
    for col in range(length):
        new_row=''.join(stamp[length-row-1][col] for row in range(length))
        rotated.append(new_row)
    return rotated


T=int(input())
for _ in range(T):
    flag=False
    space=input()
    N=int(input())
    desired_painting=[]
    for _ in range(N):
        desired_painting.append(input().strip())
    
    K=int(input())
    og_stamp=[]
    for _ in range(K):
        og_stamp.append(input().strip())
    
    our_painting=[]
    for _ in range(N):
        string=""
        for _ in range(N):
            string+="."
        our_painting.append(string)

    stamp=og_stamp[:]
    for rotation in range(4):
        if rotation>0:
            stamp=rotate_90(stamp)
    # i∈[1,N−K+1] and j∈[1,N−K+1]
        for i in range(N-K+1):
        #0-based indexing i think?
            for j in range(N-K+1):

            # cur_painting=our_painting
            # for stamp_orient in range(4):
            #     for rotates in range(stamp_orient):
            #         stamp=rotate_90(stamp)
                cur_painting = [row[:] for row in our_painting]
                for row in range(K):
                    for col in range(K):
                        if stamp[row][col]=="*": 
                            string=cur_painting[i+row]
                            string=string[:j+col]+"*"+string[j+col+1:]
                            cur_painting[i+row]=string
            

            #check if our paitning is on the right track
                on_track=True
                for r in range(N):
                    for c in range(N):
                        if cur_painting[r][c]=="*" and desired_painting[r][c]==".":
                            on_track=False
                            break

                if on_track:
                    our_painting=cur_painting
                if our_painting==desired_painting:
                    flag=True
                    print("YES")
                    break
            if flag:
                break
        if flag:
            break
    if not flag:       
        print("NO")