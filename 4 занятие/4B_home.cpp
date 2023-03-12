#include <bits/stdc++.h>

using namespace std;

int main() {
    map<string, int> d;

    int n;
    cin >> n;

    for (int i = 0; i < n; i++) {
        int q;
        cin >> q;
        if (q == 1) {
            int t;
            string name;
            cin >> name >> t;
            d[name] += t;
        } else if (q == 2) {
            string name;
            cin >> name;
            if (d.find(name) == d.end()) {
                cout << "ERROR\n";
            } else {
                cout << d[name] << "\n";
            }
        }
    }
}
