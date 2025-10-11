import sys

sys.stdin = open("evolution.in", "r")
sys.stdout = open("evolution.out", "w")

N = int(sys.stdin.readline())
subpops = []
for _ in range(N):
    parts = sys.stdin.readline().strip().split()
    items = parts[1:]
    subpops.append(set(items))

# Map features to populations containing them
feature_map = {}
for idx, feats in enumerate(subpops):
    for f in feats:
        feature_map.setdefault(f, set()).add(idx)

# Check for any crossing pair
valid = True
features = list(feature_map.keys())
M = len(features)

for i in range(M):
    for j in range(i + 1, M):
        f1 = features[i]
        f2 = features[j]
        S1 = feature_map[f1]
        S2 = feature_map[f2]
        # Determine counts for each category
        both = S1 & S2
        only1 = S1 - S2
        only2 = S2 - S1
        if both and only1 and only2:
            valid = False
            break
    if not valid:
        break

print("yes" if valid else "no")
