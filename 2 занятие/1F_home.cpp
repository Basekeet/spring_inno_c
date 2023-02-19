#include <bits/stdc++.h>

using namespace std;

int main (){
    ifstream fin("input.txt");
    ofstream fout("output.txt");

    long double r, g, b, c, m, y, k, R_, G_, B_;
    
    fin >> r >> g >> b;
    
    if (r + g + b == 0) {
        fout << 0 << " " << 0 << " " << 0 << " " << 1; 
        return 0;
    }
    R_ = r / 255.0;
    G_ = g / 255.0;
    B_ = b / 255.0;

    k = 1 - max(R_, max(G_, B_));
    c = (1 - R_ - k) / (1 - k);
    m = (1 - G_ - k) / (1 - k);
    y = (1 - B_ - k) / (1 - k);

    fout << setprecision(15) << c << " " << m << " " << y << " " << k;

}