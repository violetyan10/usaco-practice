def generate_permutations(blocks_list):
        if len(blocks_list) == 1:
            return [blocks_list]
        else:
            permutations = []
            for i in range(len(blocks_list)):
                for perm in generate_permutations(blocks_list[:i] + blocks_list[i+1:]):
                    permutations.append([blocks_list[i]] + perm)
            return permutations

N=int(input())
dictionary=[]
for _ in range(4):
    dictionary.append(input().strip())

dictionary=sorted(dictionary)

#print(generate_permutations(dictionary))

for _ in range(N):
    word=input()
    flag=False
    for perm in generate_permutations(dictionary):
        work=True
        for i in range(len(word)):
            #if word!= perm:
            if word[i] not in perm[i]:
                work=False
                break
        if work:
            flag=True
            print("YES")
            break
    if not flag:
        print("NO")