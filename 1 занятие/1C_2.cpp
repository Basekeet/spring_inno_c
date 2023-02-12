#include <bits/stdc++.h>

using namespace std;

typedef long double ld;

int main() {
    string n;
    cin >> n;

    int s = 0;

    for (int i = 0; i < n.size(); i++) {
        s += n[i] - 48;
    }
    cout << s;
}