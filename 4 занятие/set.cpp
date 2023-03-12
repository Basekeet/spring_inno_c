#include <bits/stdc++.h>

using namespace std;

int main() {
    set<int> s;

    s.insert(1);
    s.insert(3);
    s.insert(-5);
    s.insert(0);
    
    for (auto el : s) {
        cout << el << "\n";
    }
}
