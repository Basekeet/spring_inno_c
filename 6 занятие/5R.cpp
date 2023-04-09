#include <bits/stdc++.h>

using namespace std;

int n;

void f(int i) {
    if (i == n) {
        return;
    }
    int tmp;
    cin >> tmp;
    f(i + 1);
    cout << tmp << " ";
}

int main() {
    cin >> n;
    f(0);
}
