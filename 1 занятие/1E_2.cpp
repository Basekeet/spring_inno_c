#include <bits/stdc++.h>

using namespace std;

int main() {
    string n;
    cin >> n;
    reverse(n.begin(), n.end());
    int i = 0;
    while (n[i] == '0') {
        i++;
    }

    for (;i < n.size(); i++) {
        cout << n[i];
    }
}   