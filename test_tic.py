import sys

sys.stdin = open("tttt.in", "r")
sys.stdout = open("tttt.out", "w")

board = [list(sys.stdin.readline().strip()) for _ in range(3)]

individual_winners = set()
team_wins = set()

def check_win(line):
    line_set = set(line)
    if len(line_set) == 1:
        individual_winners.add(line[0])
    elif len(line_set) == 2:
        a, b = sorted(line_set)
        team_wins.add((a, b))

# Check rows
for row in board:
    check_win(row)

# Check columns
for col in range(3):
    col_list = [board[row][col] for row in range(3)]
    check_win(col_list)

# Check diagonals
check_win([board[i][i] for i in range(3)])
check_win([board[i][2 - i] for i in range(3)])

# Filter out teams that contain any individual winner
filtered_teams = {team for team in team_wins if team[0] not in individual_winners and team[1] not in individual_winners}

# # DEBUG prints - comment out or remove before submitting
# print("Individual winners:", individual_winners, file=sys.stderr)
# print("All teams found:", team_wins, file=sys.stderr)
# print("Filtered teams:", filtered_teams, file=sys.stderr)

print(len(individual_winners))
print(len(filtered_teams))
