#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    stack<int> s;
    int n;
    cin >> n;

    for (int i = 0; i < n; i++) {
        int c;
        cin >> c;
        if (c == 1) {
            int t;
            cin >> t;
            if (s.empty()) {
                s.push(t);
            } else {
                s.push(min(s.top(), t));
            }
        } else if (c == 2) {
            s.pop();
        } else {
            cout << s.top() << "\n";
        }
    }
}
