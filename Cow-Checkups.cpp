// #include <bits/stdc++.h>
// using namespace std;

// int main() {
//     ios::sync_with_stdio(false);
//     cin.tie(nullptr);

//     int N;
//     cin >> N;

//     vector<int> cow(N), need(N);
//     for (int i = 0; i < N; i++) cin >> cow[i];
//     for (int i = 0; i < N; i++) cin >> need[i];

//     // Step 1: original matches and prefix sum
//     vector<int> base(N), pref(N + 1, 0);
//     for (int i = 0; i < N; i++) {
//         base[i] = (cow[i] == need[i]);
//         pref[i + 1] = pref[i] + base[i];
//     }

//     // Step 2: diagonal prefix sums
//     // diag[s][i] = number of matches cow[k] == need[s-k] for k in [0, i)
//     vector<vector<int>> diag(2 * N - 1, vector<int>(N + 1, 0));

//     for (int s = 0; s < 2 * N - 1; s++) {
//         for (int i = 0; i < N; i++) {
//             diag[s][i + 1] = diag[s][i];
//             int j = s - i;
//             if (0 <= j && j < N && cow[i] == need[j]) {
//                 diag[s][i + 1]++;
//             }
//         }
//     }

//     // Step 3: count all reversals
//     vector<long long> ans(N + 1, 0);

//     for (int l = 0; l < N; l++) {
//         for (int r = l; r < N; r++) {
//             int outside = pref[l] + (pref[N] - pref[r + 1]);
//             int s = l + r;
//             int inside = diag[s][r + 1] - diag[s][l];
//             int total = outside + inside;
//             ans[total]++;
//         }
//     }

//     // Output
//     for (int i = 0; i <= N; i++) {
//         cout << ans[i] << '\n';
//     }

//     return 0;
// }

#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    vector<int> cow(N), need(N);
    for (int i = 0; i < N; i++) cin >> cow[i];
    for (int i = 0; i < N; i++) cin >> need[i];

    // prefix matches (same as Python)
    vector<int> pref(N + 1, 0);
    for (int i = 0; i < N; i++) {
        pref[i + 1] = pref[i] + (cow[i] == need[i]);
    }

    vector<long long> ans(N + 1, 0);
    vector<int> diag(N + 1);   // reused diagonal buffer

    // iterate diagonals in increasing s = l + r
    for (int s = 0; s < 2 * N - 1; s++) {

        // build diag[s][*]
        diag[0] = 0;
        for (int i = 0; i < N; i++) {
            diag[i + 1] = diag[i];
            int j = s - i;
            if (0 <= j && j < N && cow[i] == need[j]) {
                diag[i + 1]++;
            }
        }

        // EXACT same (l, r) logic, just grouped by s
        for (int l = max(0, s - (N - 1)); l <= min(N - 1, s); l++) {
            int r = s - l;
            if (l > r) continue;   // matches original l <= r condition

            int out = pref[l] + (pref[N] - pref[r + 1]);
            int ins = diag[r + 1] - diag[l];
            ans[out + ins]++;
        }
    }

    for (int i = 0; i <= N; i++) {
        cout << ans[i] << '\n';
    }

    return 0;
}
