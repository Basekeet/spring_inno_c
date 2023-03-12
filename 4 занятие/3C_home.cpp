#include <bits/stdc++.h>

using namespace std;

int main() {
    string st;
    cin >> st;

    stack<char> s;

    for (auto c : st) {
        if (c == '(' || c == '[' || c == '{') {
            s.push(c);
        } else if (s.size() == 0) {
            cout << "NO";
            return 0;
        } else {
            if (c == ')' && s.top() != '(' ||
                c == ']' && s.top() != '[' ||
                c == '}' && s.top() != '{') {
                    cout << "NO";
                    return 0;
            } else {
                s.pop();
            }
        }
    }
    if (s.size() != 0) {
        cout << "NO";
    } else {
        cout << "YES";
    }
}
