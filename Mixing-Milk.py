import sys

sys.stdin = open("mixmilk.in", "r")
sys.stdout = open("mixmilk.out", "w")

buckets=[]
bucket=[]

for i in range(3):
    buckets.append(list(map(int,input().split()))) #input
    bucket.append(buckets[i][1]) #initial milk

for i in range (100):
    first=i%3
    second=(i+1)%3
    space=buckets[second][0]-bucket[second]
    poured=min(bucket[first],space)
    bucket[first]-=poured
    bucket[second]+=poured

for i in range(3):
    print(str(bucket[i]))