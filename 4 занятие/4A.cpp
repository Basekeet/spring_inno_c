#include <bits/stdc++.h>

using namespace std;

int main() {
    priority_queue<int> pq;

    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        int t;
        cin >> t;
        if (t == 0) {
            int q;
            cin >> q;
            pq.push(q);
        } else if (t == 1) {
            cout << pq.top() << "\n";
            pq.pop();
        }
    }
}
