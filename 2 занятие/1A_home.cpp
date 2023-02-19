#include <bits/stdc++.h>

using namespace std;

int main (){
    ifstream fin("input.txt");
    ofstream fout("output.txt");

    long double f, c;
    fin >> f >> c;
    long double res_c, res_f;
    res_c = 5.0 / 9.0 * (f - 32);
    res_f = 9.0 / 5.0 * c + 32;
    fout << setprecision(15) << res_c << "\n" << res_f;
}