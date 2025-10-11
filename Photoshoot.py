N=int(input())
photo=input().strip() #hg
string=[]
#go through pairs dont care abt gg hh want to keep hg and flip gh
for i in range(0,N,2):
    if photo[i:i+2]=="GG" or photo[i:i+2]=="HH":
        continue
    if photo[i:i+2]=="GH":
        string.append(1)
    else:
        string.append(0)

#flip gh
#condense thy groups
#if last part fine we can remove from thy list

flips=0
while True:
    new_string=[]
    for c in string:
        if len(new_string)==0:
            new_string.append(c)
        elif c!=new_string[-1]:
            new_string.append(c)
    string=new_string
    if string[-1]==0:
        string.pop()
    string.reverse()
    for i in range(len(string)):
        if string[i]==0:
            string[i]=1
        else:
            string[i]=0
    if len(string)==0:
        break
    flips+=1
print(flips)