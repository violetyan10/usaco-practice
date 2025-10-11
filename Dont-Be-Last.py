import sys

sys.stdin = open("notlast.in", "r")
sys.stdout = open("notlast.out", "w")

cows = ["Bessie", "Elsie", "Daisy", "Gertie", "Annabelle", "Maggie", "Henrietta"]

N = int(sys.stdin.readline())
milking_log={cow: 0 for cow in cows}
for _ in range(N):
    name, amount = sys.stdin.readline().strip().split()
    amount = int(amount)
    milking_log[name] += amount

minimum=min(milking_log.values())
if len(set(milking_log.values()))==1:
    print("Tie")
    exit()

milking_log ={key: value for key, value in milking_log.items() if value != minimum}
num_return=min(milking_log.values())


matches = [k for k, v in milking_log.items() if v == num_return]
if len(matches)==1:
    print(matches[0])
else:
    print("Tie")
