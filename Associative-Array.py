Q=int(input())
queries=[]
for _ in range (Q):
    queries.append(list(map(int,input().split())))

a={}
for query in queries:
    length=len(query)
    if length==3:
        _,k,v=query
        if k not in a:
            a[k]=0
        a[k]=v
    else:
        _,k=query
        if k not in a:
            print(0)
        else:
            print(a[k])