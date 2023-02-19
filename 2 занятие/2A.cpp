#include <bits/stdc++.h>

using namespace std;

int main (){
    int n, k;
    cin >> n >> k;

    vector<int> v;
    for (int i = 0; i < n; i++) {
        int tmp;
        cin >> tmp;
        v.push_back(tmp);
    }

    for (int i = 0; i < k; i++) {
        int tmp;
        cin >> tmp;

        int l = 0;
        int r = n;

        while (r - l > 1) {
            int mid = (r + l) / 2;
            if (v[mid] > tmp) {
                r = mid;
            } else {
                l = mid;
            }
        }
        if (v[l] == tmp) {
            cout << "YES\n";
        } else  {
            cout << "NO\n";
        }

    }
}