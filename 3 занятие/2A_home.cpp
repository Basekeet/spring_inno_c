#include <bits/stdc++.h>

using namespace std;

int main() {
    int n;
    cin >> n;

    vector<int> v;

    for (int i = 0; i < n; i++) {
        int t;
        cin >> t;
        v.push_back(t);
    }
    sort(v.begin(), v.end());
    int q;
    cin >> q;
    for (int i = 0; i < q; i++) {
        int a, b;
        cin >> a >> b;

        int l = -1;
        int r = n;

        while (r - l > 1) {
            int mid = (r + l) / 2;
            if (v[mid] >= a) {
                r = mid;
            } else {
                l = mid;
            }
        }

        int left = r;

        l = -1;
        r = n; 
        while (r - l > 1) {
            int mid = (r + l) / 2;

            if (v[mid] > b) {
                r = mid;
            } else {
                l = mid;
            }
        }
        int right = r;
        cout << (right - left) << " ";
    }
}
