N,F=map(int, input().split())
contest=input().strip()

possible=dict()
works=set()

for i in range(N-2):
    first=contest[i]
    sec=contest[i+1]
    third=contest[i+2]
    if sec==third and first!=sec:
        temp=contest[i:i+3]
        if temp in possible:
            possible[temp].append(i)
        else:
            possible[temp]=[i]


for k,v in possible.items():
    if len(v)>=F:
        works.add(k)

for k,v in possible.items():
    if len(v)==F-1:
        x,y=k[0],k[1]
        used=set()
        for index in v:
            used.add(index)
            used.add(index+1)
            used.add(index+2)

        for i in range(N-2):
            if i in used or i+1 in used or i+2 in used:
                continue
            first=contest[i]
            sec=contest[i+1]
            third=contest[i+2]
            change=0
            if first!=x:
                change+=1
            if sec!=y:
                change+=1
            if third!=y:
                change+=1
            if change==1:
                works.add(k)
                break

if F==1:
    for i in range(N-2):
        first=contest[i]
        sec=contest[i+1]
        third=contest[i+2]
        if sec==third:
            for ch in range(26):
                x=chr(ord("a")+ch)
                if x!=sec:
                    works.add(x+sec+sec)

ans=sorted(works)
print(len(ans))
for w in ans:
    print(w)