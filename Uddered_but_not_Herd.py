cowphabet=input().strip()
heard=input().strip()

index=0
count=1
for i in range(len(heard)):
    letter=heard[i]
    where=cowphabet.find(letter)
    if where<=index:
        count+=1
    index=where
print(count)