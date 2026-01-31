#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, K;
    cin >> N >> K;

    int Q;
    cin >> Q;

    vector<vector<int>> board(N, vector<int>(N, 0));
    vector<vector<int>> sums(N, vector<int>(N, 0));

    int maxval = 0;

    while (Q--) {
        int r, c, v;
        cin >> r >> c >> v;
        --r; --c;  // to 0-based

        int diff = v - board[r][c];
        board[r][c] = v;

        for (int a = max(r - K + 1, 0); a <= min(r, N - K); ++a) {
            for (int b = max(c - K + 1, 0); b <= min(c, N - K); ++b) {
                sums[a][b] += diff;
                maxval = max(maxval, sums[a][b]);
            }
        }

        cout << maxval << '\n';
    }
    return 0;
}
