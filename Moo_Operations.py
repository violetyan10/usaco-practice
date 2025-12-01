# Q=int(input())
# strings=[]
# for _ in range(Q):
#     strings.append(input().strip())

# for string in strings:
#     count=0
#     #goes thorugh strings
#     new_string=list(string)

#     left=0
#     right=len(new_string)-1

#     while right-left+1>3:
#         if new_string[left]=="M":
#             count+=1
#             right-=1
#         elif new_string[right]=="O":
#             count+=1
#             left+=1
#         elif new_string[left]=="O":
#             count+=1
#             right-=1
#             new_string[right+1]="M"
#         else:
#             count+=1
#             left+=1
#             new_string[left-1]="O"
#     new_string=new_string[left:right+1]


#     if len(new_string)==3:
#         if new_string[1]!="M":
#             if new_string[-1]=="M":
#                 count+=1
#             if new_string[0]=="O":
#                 count+=1
#             print(count)
#         else:
#             print(-1)
#     else:
#         print(-1)
Q=int(input())
strings=[]
for _ in range(Q):
    strings.append(input().strip())

for string in strings:
    count=-1
    if "MOO" in string:
        count=len(string)-3
    elif "MOM" in string or "OOO" in string:
        count=len(string)-2
    elif "OOM" in string:
        count=len(string)-1
    print(count)