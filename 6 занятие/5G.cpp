#include <bits/stdc++.h>

using namespace std;

string solve(int a, int b) {
    if (a == b) {
        return to_string(a);
    } else if (b % 2 != 0 || b < 2 * a) {
        return "(" + solve(a, b - 1) + " + 1)";
    } else {
        return solve(a, b / 2) + " * 2";
    }
}

int main() {
    int a, b;
    cin >> a >> b;
    cout << b << " = " << solve(a, b) << "\n";
}
