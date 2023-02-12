#include <bits/stdc++.h>

using namespace std;

int main() {
    int d, m;
    cin >> d >> m;

    if ((m == 10 && d >= 26) || (m == 11 && d <= 7)) {
        cout << "true";
    } else {
        cout << "false";
    }
}