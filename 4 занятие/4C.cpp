#include <bits/stdc++.h>

using namespace std;

int main() {
    int n;
    cin >> n;
    pair<int, int> p[n];

    for (int i = 0; i < n; i++) {
        cin >> p[i].first >> p[i].second;
    }
    sort(p, p + n);

    set<pair<char, int>> s;
    for (int i = 1; i < n; i++) {
        if (p[i].first == p[i - 1].first) {
            s.insert({'y', p[i].second});
        } else {
            s.insert({'x', p[i].first});
        }
    }
    cout << s.size() << "\n";
    for (auto el : s) {
        cout << el.first << " " << el.second << "\n";
    }
}
