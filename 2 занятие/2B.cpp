#include <bits/stdc++.h>

using namespace std;

int main() {
    int n;
    cin >> n;

    int l = 1;
    int r = n + 1;
    while (true) {
        int mid = (r + l) / 2;
        cout << mid << endl;
        int t;
        cin >> t;

        if (t == -1) {
            r = mid;
        } else if (t == 1) {
            l = mid;
        } else {
            return 0;
        }
    }

}