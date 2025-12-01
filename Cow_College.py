# N=int(input())
# tuitions=list(map(int,input().split()))
# maxp=0
# tuition=100000000
# for pay in tuitions:
#     cur_max=0
#     for c in tuitions:
#         if c>=pay:
#             cur_max+=pay
#     #print(cur_max)

#     if cur_max>maxp:
#         maxp=cur_max
#         tuition=pay
#     if maxp==cur_max:
#         tuition=min(pay,tuition)
    
# print(maxp,tuition)
N=int(input())
tuitions=sorted(list(map(int,input().split())))
maxp=0
tuition=100000000
for i in range(len(tuitions)):
    cur_max=(N-i)*tuitions[i]
    if cur_max>maxp:
        maxp=cur_max
        tuition=tuitions[i]
    if maxp==cur_max:
        tuition=min(tuitions[i],tuition)
    
print(maxp,tuition)