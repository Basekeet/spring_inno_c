#include <bits/stdc++.h>

using namespace std;

int main() {
    int n;
    cin >> n;
    int s = 0;
    int MAX = -1;

    for (int i = 0; i < n; i++) {
        int t;
        cin >> t;
        MAX = max(MAX, t);
        s += t;
    }
    cout << s - MAX;
}