#include <set>
#include <map>
#include <ctime>
#include <cstdio>
#include <vector>
#include <string>
#include <climits>
#include <cstdlib>
#include <cstddef>
#include <sstream>
#include <string.h>
#include <iostream>
#include <algorithm>

#define LL long long

template <typename T> T sqr(T x) { return x * x; }
template <typename T> T abs(T x) { return x < 0 ? -x : x; }
template <typename T> T _min(T a, T b) { return a < b ? a : b; }
template <typename T> T _max(T a, T b) { return a > b ? a : b; }

using namespace std;

#define N 1010

int f[N][N * 10], c[N], w[N];
vector<int> ans;
int n, m;

void print_ans(int n, int m)
{
	if (f[n][m] == 0)
		return;
	
	if (f[n - 1][m] == f[n][m])
		print_ans(n - 1, m);
	else
	{
		print_ans(n - 1, m - w[n]);
		ans.push_back(n);
	}
}

int main()
{
/*
	freopen("knapsack.in", "r", stdin);
	freopen("knapsack.out", "w", stdout);
*/
	cin>> n>> m;
	for (int i = 1; i <= n; i++)
		scanf("%d", &w[i]);
	for (int i = 1; i <= n; i++)
		scanf("%d", &c[i]);
	f[0][0] = 0;
	for (int i = 1; i <= n; i++)
		for (int j = 0; j <= m; j++)
		{
			f[i][j] = f[i - 1][j];
			if (j >= w[i] && f[i - 1][j - w[i]] + c[i] > f[i][j])
				f[i][j] = f[i - 1][j - w[i]] + c[i];
		}

	print_ans(n, m);
	cout<< ans.size()<< endl;
	for (int i = 0; i < (int) ans.size() - 1; i++)
		printf("%d ", ans[i]);

	if (ans.size() > 0)
		cout<< ans[ans.size() - 1]<< endl;

	return 0;
}
