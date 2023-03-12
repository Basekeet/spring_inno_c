#include<bits/stdc++.h>

using namespace std;

int main() {
    deque<int> a[150001];

    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        string s;
        cin >> s;
        int a1, a2;
        if (s == "pushback") {
            cin >> a1 >> a2;
            a[a1].push_back(a2);
        } else if (s == "pushfront") {
            cin >> a1 >> a2;
            a[a1].push_front(a2);
        } else if (s == "popback") {
            cin >> a1;
            cout << a[a1].back() << "\n";
            a[a1].pop_back();
        } else {
            cin >> a1;
            cout << a[a1].front() << "\n";
            a[a1].pop_front();
        }
    }
}
