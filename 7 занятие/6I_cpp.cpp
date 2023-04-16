#include <bits/stdc++.h>

using namespace std;

const int NEG_INF = -10000000;

int C[1001][1001];
int dp[1001][10001];
char dp_r[1001][1001];

int main() {
    int n, m;
    cin >> n >> m;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> C[i][j];
        }
    }

    memset(dp, NEG_INF, sizeof(int) * 1001 * 1001);

    dp[0][0] = 0;
    dp_r[0][0] = 0;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (i != 0 && dp[i - 1][j] > dp[i][j]) {
                dp[i][j] = dp[i - 1][j];
                dp_r[i][j] = 'D';
            }

            if (j != 0 && dp[i][j - 1] > dp[i][j]) {
                dp[i][j] = dp[i][j - 1];
                dp_r[i][j] = 'R';
            }

            dp[i][j] += C[i][j];
        }
    }
    cout << dp[n - 1][m - 1] << "\n";
    n--;
    m--;
    string ans = "";
    while (dp_r[n][m] != 0) {
        ans = dp_r[n][m] + ans;
        if (dp_r[n][m] == 'D') {
            n--;
        } else {
            m--;
        }
    }
    cout << ans;
}
