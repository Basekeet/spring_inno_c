#include <bits/stdc++.h>

using namespace std;

int main() {
    deque<int> d1;
    deque<int> d2;

    int n;
    cin >> n;
    for (int i = 0 ; i < n; i++) {
        char a;
        cin >> a;
        if (a == '+') {
            int t;
            cin >> t;
            d2.push_back(t);
        } else if (a == '*') {
            int t;
            cin >> t;
            d2.push_front(t);
        } else {
            cout << d1.front() << "\n";
            d1.pop_front();
        }
        
        if (d1.size() < d2.size()) {
            d1.push_back(d2.front());
            d2.pop_front();
        }
    }
}
