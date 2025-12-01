correct=[]
for _ in range(3):
    correct.append(input().strip())

guess=[]
for _ in range(3):
    guess.append(input().strip())

greens=0

for row in range(3):
    for col in range(3):
        if correct[row][col]==guess[row][col]:
            greens+=1
            guess[row]=guess[row][:col]+"!"+guess[row][col+1:]
            correct[row]=correct[row][:col]+"!"+correct[row][col+1:]

yellows=0

print(greens)


correct_list = []
guess_list=[]

for row in range(3):
    for col in range(3):
        char=correct[row][col]
        correct_list.append(ord(char)-ord('A')+1)

for row in range(3):
    for col in range(3):
        char=guess[row][col]
        guess_list.append(ord(char)-ord('A')+1)

correct_list.sort()
guess_list.sort()

# print(correct_list)
# print(guess_list)

while correct_list:
    count=0
    second_count=0
    num=correct_list[0]
    if num<=0:
        correct_list.remove(num)
        if num in guess_list:
            guess_list.remove(num)
        continue
    while num in correct_list:
        correct_list.remove(num)
        count+=1
    while num in guess_list:
        guess_list.remove(num)
        second_count+=1
    
    if second_count>count:
        yellows+=count
    else:
        yellows+=second_count

print(yellows)