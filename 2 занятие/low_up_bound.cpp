#include <bits/stdc++.h>

using namespace std;

int lower_bound(int k, const vector<int>& res) {
    int l = -1;
    int r = res.size();

    while (r - l > 1) {
        int mid = (r + l) / 2;
        if (res[mid] >= k) {
            r = mid;
        } else {
            l = mid;
        }
    }

    return r;
}

int upper_bound(int k, const vector<int>& res) {
    int l = -1;
    int r = res.size();

    while (r - l > 1) {
        int mid = (r + l) / 2;
        if (res[mid] > k) {
            r = mid;
        } else {
            l = mid;
        }
    }

    return r;
}

int main() {
    int n;
    cin >> n;
    vector<int> v;

    for (int i = 0; i < n; i++) {
        int tmp;
        cin >> tmp;
        v.push_back(tmp);
    }

    int a = 3;
    int b = 9;

    cout << lower_bound(a, v) << "\n";
    cout << upper_bound(b, v);


}