#include <bits/stdc++.h>

using namespace std;

int main() {
    int n1, n2;
    int res = 0;

    cin >> n1;
    while (true) {
        cin >> n2;
        if (n2 == 0) {
            break;
        }

        if (n1 < n2) {
            res++;
        }
        n1 = n2;
    }
    cout << res;
}