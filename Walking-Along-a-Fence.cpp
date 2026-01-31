#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, P;
    cin >> N >> P;

    vector<pair<int,int>> posts(P);
    for (auto &p : posts) cin >> p.first >> p.second;

    vector<array<int,4>> cows(N);
    for (auto &c : cows)
        for (int &x : c) cin >> x;

    vector<pair<int,int>> fence;
    fence.reserve(200000); // safe upper bound for grid-style fences

    for (int i = 0; i < P; i++) {
        auto cur = posts[i];
        auto nxt = posts[(i + 1) % P];
        fence.push_back(cur);

        if (cur.first == nxt.first) { // vertical
            int dir = (cur.second < nxt.second) ? 1 : -1;
            for (int y = cur.second + dir; y != nxt.second; y += dir)
                fence.push_back({cur.first, y});
        } else { // horizontal
            int dir = (cur.first < nxt.first) ? 1 : -1;
            for (int x = cur.first + dir; x != nxt.first; x += dir)
                fence.push_back({x, cur.second});
        }
    }

    // Map fence point -> index
    unordered_map<long long, int> index;
    index.reserve(fence.size());

    auto encode = [](int x, int y) {
        return (long long)x << 32 | (unsigned int)y;
    };

    for (int i = 0; i < (int)fence.size(); i++) {
        index[encode(fence[i].first, fence[i].second)] = i;
    }

    int L = fence.size();

    for (auto &c : cows) {
        int s = index[encode(c[0], c[1])];
        int e = index[encode(c[2], c[3])];

        int d = abs(e - s);
        cout << min(d, L - d) << "\n";
    }

    return 0;
}
