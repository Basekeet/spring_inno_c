#include <bits/stdc++.h>

using namespace std;

int main() {
    string s;
    cin >> s;

    string res = "";

    // for i in range(len(s)):
    for (int i = 0; i < s.size(); i++) {
        res = s[i] + res;
    }

    cout << res;
}