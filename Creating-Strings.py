string=input()
outputs=[]

letters=[0]*26

for letter in string:
    letters[ord(letter) - ord('a')]+=1

def permutation(cur=""):
	for i in range(26):
		if letters[i] > 0:
			letters[i] -= 1
			permutation(cur + chr(ord("a") + i))
			letters[i] += 1
	if len(string)==len(cur):
		outputs.append(cur)
		return
	
permutation()
print(len(outputs))
for output in outputs:
	print(output)