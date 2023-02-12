#include <bits/stdc++.h>

using namespace std;

typedef long double ld;

int main() {
    ld x, y;
    cin >> x >> y;

    ld res = sqrt(x * x + y * y);
    cout << setprecision(10) << res;
}