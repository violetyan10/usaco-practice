N=int(input())
S=input().strip()

mini=0
maxi=0

#location
index=0

while index<N:
    #if f we dont care
    if S[index]=="F":
        index+=1
        continue

    #checking if theres like a chain of fs after
    j=index+1
    while j<N and S[j]=="F":
        j+=1
    if j==N:
        break

    #how many fs in a row + endpoints (length of block)
    length=j-index+1

    #patterns BFFFFB
    if S[index]==S[j]:
        if length%2==0:
            mini+=1
        maxi+=length-1
    #pattenrs like BFFFE
    else:
        if length%2==1:
            mini+=1
        maxi+=length-2

    index=j


#lead and trail fs
leading=len(S)-len(S.lstrip('F'))
trailing=len(S)-len(S.rstrip('F'))

if leading==N:  #all fs
    mini=0
    maxi=N-1
else:
    maxi+=leading+trailing #expand if trail and lead fs

#not free end
if leading==0 and trailing==0:
    possible=[]
    for idk in range(mini,maxi+1,2):
        possible.append(idk)
#free end make flexible
else:
    possible=[]
    for idk in range(mini,maxi+1):
        possible.append(idk)

print(len(possible))
for a in range(len(possible)):
    print(possible[a])