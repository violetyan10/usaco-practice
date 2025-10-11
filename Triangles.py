import sys

sys.stdin = open("triangles.in", "r")
sys.stdout = open("triangles.out", "w")

N=(int(sys.stdin.readline()))

posts=[]
for _ in range(N):
    posts.append((list(map(int,sys.stdin.readline().split()))))


# max_area=0
# for point in posts:
#     x,y=point
#     max_x=0
#     max_y=0
#     for x0 in posts:
#         if x0!=point:
#             x_val=x0[0]
#             y_val=x0[1]
#             if y==y_val:
#                 if abs(x_val-x)>max_x:
#                     max_x=abs(x_val-x)         
#     for y0 in posts:
#         if y0!=point:
#             x_val=y0[0]
#             y_val=y0[1]
#             if x==x_val:
#                 if abs(y_val-y)>max_y:
#                     max_y=abs(y_val-y)
#     max_area=max(max_area,max_x*max_y)
# print(max_area)

max_area=0
for point in posts:
    x,y=point
    max_x=0
    max_y=0
    for two in posts:
        if two!=point:
            x_val=two[0]
            y_val=two[1]
            if x==x_val:
                max_y=max(max_y,abs(y_val-y))
            if y==y_val:
                max_x=max(max_x,abs(x_val-x))      
    max_area=max(max_area,max_x*max_y)
print(max_area)