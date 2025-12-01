# N=int(input())
# cows=input()
# Es=list(map(int,input().split()))
# breeds=[]
# Gs=[]
# Hs=[]


# for i in range(N): #g=0 and h=1
#     if cows[i]=="G":
#         breeds.append(0)
#         Gs.append(i)
#     else:
#         breeds.append(1)
#         Hs.append(i)

# #print(Gs,Hs)
# count=0
# #print(breeds)
# flag=False
# for G in Gs:
#     for H in Hs:
#         G_list=Es[G]
#         all_gs=[]
#         for g_cow in range(G,G_list):
#             if g_cow==H:
#                 flag=True
#                 break
#             all_gs.append(g_cow)
#         if all_gs==Gs:
#             flag=True
#         new_flag=False
#         if flag:
#             #print("idk")
#             H_list=Es[H]
#             all_hs=[]
#             for h_cow in range(H,H_list):
#                 if h_cow==G:
#                     new_flag=True
#                     break
#                 all_hs.append(h_cow)
#             if all_hs==Hs:
#                 new_flag=True
#         if new_flag:
#             count+=1

# print(count)

# N=int(input())
# cows=input()
# Es=list(map(int,input().split()))
# breeds=[]
# Gs=[]
# Hs=[]


# for i in range(N): #g=0 and h=1
#     if cows[i]=="G":
#         breeds.append(0)
#         Gs.append(i)
#     else:
#         breeds.append(1)
#         Hs.append(i)

# #print(Gs,Hs)
# count=0
# #print(breeds)
# G_count=0
# H_count=0
# for G in Gs:
#     G_list=Es[G]
#     all_gs=[]
#     for g_cow in range(G,G_list):
#         if g_cow not in Gs:
#             G_count+=1
#             break
#         all_gs.append(g_cow)
#         if all_gs==Gs:
#             G_count+=1

# for H in Hs:
#     H_list=Es[H]
#     all_hs=[]
#     for h_cow in range(H,H_list):
#         if h_cow not in Hs:
#             H_count+=1
#             break
#         all_hs.append(h_cow)
#         if all_hs==Hs:
#             H_count+=1
# print(H_count*G_count)

# N=int(input())
# cows=input()
# Es=list(map(int,input().split()))
# Es = [e - 1 for e in Es]
# breeds=[]
# Gs=[]
# Hs=[]


# for i in range(N): #g=0 and h=1
#     if cows[i]=="G":
#         breeds.append(0)
#         Gs.append(i)
#     else:
#         breeds.append(1)
#         Hs.append(i)

# #print(Gs,Hs)
# count=0
# #print(breeds)
# g_lead=[]
# G_count=0
# H_count=0
# for G in Gs:
#     flag=False
#     G_list=Es[G]
#     all_gs=[]
#     for g_cow in range(G,G_list+1):
#         if g_cow not in Gs:
#             G_count+=1
#             flag=True
#             break
#         else:
#             all_gs.append(g_cow)
#         if all_gs==Gs:
#             G_count+=1
#             flag=True
#     if flag:
#         g_lead.append(G)


# for H in Hs:
#     H_list=Es[H]
#     all_hs=[]
#     for h_cow in range(H,H_list+1):
#         if h_cow in g_lead:
#             H_count+=1
#             break
#         else:
#             all_hs.append(h_cow)
#         if all_hs==Hs:
#             H_count+=1
# print(H_count*G_count)

N=int(input())
cows=input()
Es=list(map(int, input().split()))
Es=[e-1 for e in Es]

lastG,lastH,firstG,firstH =-1,-1,-1,-1

for i in range(N-1,-1,-1):
    if cows[i]=='G':
        lastG=i
    if cows[i]=='H':
        lastH=i

for i in range(N):
    if cows[i]=='G':
        firstG=i
    if cows[i]=='H':
        firstH=i

pairs=0

#g
if Es[lastG]>=firstG:
    for i in range(lastG):
        if i==lastH:
            continue
        if cows[i]=='H' and Es[i]>=lastG:
            pairs+=1

#h
if Es[lastH]>=firstH:
    for i in range(lastH):
        if i==lastG:
            continue
        if cows[i]=='G' and Es[i]>=lastH:
            pairs+=1

#both
if ((Es[lastG]>=firstG or (lastG<=lastH and Es[lastG]>=lastH)) and
    (Es[lastH]>=firstH or (lastH<=lastG and Es[lastH]>=lastG))):
    pairs+=1

print(pairs)
