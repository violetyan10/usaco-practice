import sys

sys.stdin = open("evolution.in", "r")
sys.stdout = open("evolution.out", "w")

N=int(sys.stdin.readline())
subpops=[]
for _ in range(N):
    parts=sys.stdin.readline().strip().split()
    items=parts[1:]
    subpops.append(set(items))

map={}
for i, feature in enumerate(subpops):
    for feat in feature:
        map.setdefault(feat,set()).add(i)

flag=True
features=list(map.keys())
num_feat=len(features)

for j in range(num_feat):
    for k in range(j+1,num_feat): #pair
        list1=map[features[j]]
        list2=map[features[k]]
        both=list1&list2
        only1=list1-list2
        only2=list2-list1
        if both and only1 and only2:
            flag=False
    if flag==False:
        break
if flag:
    print("yes")
else:
    print("no")