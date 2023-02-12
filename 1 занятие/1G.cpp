#include <bits/stdc++.h>

using namespace std;

int main() {
    long double n;
    cin >> n;

    long double res = 0;

    for (int i = 0; i < n; i++) {
        if (i % 2 == 0) {
            res += 1 / (1 + (long double)i * 2);
        } else {
            res -= 1 / (1 + (long double)i * 2);
        }
    }
    res *= 4;
    cout << setprecision(15) << res;
}   