#include <bits/stdc++.h>

using namespace std;

int main() {
    priority_queue<long long> pq;
    int n;
    cin >> n;

    for (int i = 0; i < n; i++) {
        long long t;
        cin >> t;
        pq.push(-t);
    }

    long long MAX = -1;
    while (pq.size() > 1) {
        long long a1 = -pq.top();
        pq.pop();
        long long a2 = -pq.top();
        pq.pop();
        MAX = max(a2, MAX);
        if (a1 == a2) {
            pq.push(-(a1 + a2));
        } else {
            pq.push(-a2);
        }
    }
    if (pq.size() == 1) {
        MAX = max(MAX, -pq.top());
    }

    cout << MAX;
}
