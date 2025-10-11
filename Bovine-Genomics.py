import sys

sys.stdin = open("cownomics.in", "r")
sys.stdout = open("cownomics.out", "w")

N,M = map(int, sys.stdin.readline().split())
spotty=[]
plain=[]
for _ in range(N):
    spotty.append(sys.stdin.readline().strip())
for _ in range(N):
    plain.append(sys.stdin.readline().strip())

potential=0

for i in range(M): #go through each position in all the genomes
    spotty_gen = set()
    for cow in spotty:
        spotty_gen.add(cow[i])
    plain_gen = set()
    for cow in plain:
        plain_gen.add(cow[i])
    
    if spotty_gen.isdisjoint(plain_gen):
        potential += 1

print(potential)