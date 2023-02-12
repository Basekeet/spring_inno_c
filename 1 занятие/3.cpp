#include <bits/stdc++.h>

using namespace std;

int main() {
    bool d1 = true;
    bool d2 = false;

    bool d3 = d1 && d2;
    bool d4 = d1 || d2;
    bool d5 = d1 ^ d2;
    bool d6 = !d1;

    // -2**31 - +2**31
    int a1 = -5;
    int a2 = 10;
    unsigned int a3 = 10; 

    a1++;
    a2--;
    ++a1;
    --a2;
    int a3 = (a1 + a2 * a1 / a2 - a2) % a2;
    bool a4 = a3 > a2;
    bool a5 = a3 != a2;
    bool a6 = a3 == a1;

    // -2**63 - +2**63
    long long b1 = -10;
    unsigned long long b2 = 4;

    char c1 = 'a';

    string s = "asdfasdf";
}