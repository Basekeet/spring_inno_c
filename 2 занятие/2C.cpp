#include <bits/stdc++.h>

using namespace std;
long double vp, vf, a;
const long double dx = 0.000001;

long double time(long double x) {
    return sqrt((1 - a) * (1 - a) + x * x) / vp + sqrt(a * a + (1 - x) * (1 - x)) / vf;
}

bool f(long double x) {
    return time(x) < time(x + dx);
}

int main() {
    cin >> vp >> vf >> a;

    long double l = 0;
    long double r = 1;

    while (r - l > dx) {
        long double mid = (r + l) / 2.0;

        if (f(mid)) {
            r = mid;
        } else {
            l = mid;
        }
    }

    cout << setprecision(15) << r;
}