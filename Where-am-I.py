import sys

sys.stdin = open("whereami.in", "r")
sys.stdout = open("whereami.out", "w")

N = int(sys.stdin.readline())
mailboxes=sys.stdin.readline()
for length in range(1, N+1): #length of subset we try
    seen=set()  #substrings
    flag=True
    for i in range(N-length+1):
        sub=mailboxes[i:i+length]
        if sub in seen:
            flag=False
            break
        seen.add(sub)
    if flag:
        print(length)
        break