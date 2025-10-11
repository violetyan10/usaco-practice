N=int(input())
relation=[]
for _ in range(N):
    relation.append(list(input().split()))

zodiac_cycle=["Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat",
 "Monkey", "Rooster", "Dog", "Pig", "Rat"]
zodiac_index={}
for i, animal in enumerate(zodiac_cycle):
    zodiac_index[animal]=i

birth={"Bessie":0}

for i in range(N): #i is index of cow statement
    cow=relation[i]
    new_cow=cow[0]
    direction=cow[3]
    zodiac=cow[4]
    ref=cow[7]

    ref_year=birth[ref]
    current=(ref_year%12+12)%12
    target=zodiac_index[zodiac]

    if direction=="next":
        diff=(target-current)%12
        if diff==0:
            diff=12
        birth[new_cow]=ref_year+diff
    else:  #previous
        diff=(current-target)%12
        if diff==0:
            diff=12
        birth[new_cow]=ref_year-diff
print(abs(birth["Elsie"]))