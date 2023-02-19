#include <bits/stdc++.h>

using namespace std;
int n, k;
vector<int> v;

bool f(int x) {
    int c = 1;
    int prev = v[0];

    for (int i = 1; i < v.size(); i++) {
        if (v[i] - prev >= x) {
            prev = v[i];
            c++;
        }
    }
    return c >= k;
}

int main() {
    cin >> n >> k;

    for (int i = 0; i < n; i++) {
        int t;
        cin >> t;
        v.push_back(t);
    }

    int l = 0;
    int r = v[v.size() - 1] - v[0] + 1;

    while (r - l > 1) {
        int mid = (r + l) / 2;

        if (f(mid)) {
            l = mid;
        } else {
            r = mid;
        }
    }
    cout << l;
}