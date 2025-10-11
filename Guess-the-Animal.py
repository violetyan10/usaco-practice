import sys

sys.stdin = open("guess.in", "r")
sys.stdout = open("guess.out", "w")

N=int(sys.stdin.readline())
char={}
for _ in range(N):
    parts=sys.stdin.readline().strip().split()
    key=parts[0]
    val=parts[2:]
    char[key]=list(val)

# for characteristic, animals in char.items():
#     for animal in animals:
#         if animal not in anim:
#             anim[animal] = []
#         anim[animal].append(characteristic)

# print(anim)

max=0
names=list(char.keys())

for i in range(N):
    for j in range(i+1, N):
        a1=names[i]
        a2=names[j]
        shared=len(set(char[a1])&set(char[a2]))
        if shared>max:
            max=shared
print(max+1)