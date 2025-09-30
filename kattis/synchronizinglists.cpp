#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    while (cin >> n && n > 0) {
        vector<int> la(n);
        vector<int> lb(n);

        for (int i = 0; i < n; i++) {
            cin >> la[i];
        }
        for (int i = 0; i < n; i++) {
            cin >> lb[i];
        }

        vector<int> lac = la;
        vector<int> lbc = lb;

        sort(lac.begin(), lac.end());
        sort(lbc.begin(), lbc.end());

        map<int, int> m;
        for (int i = 0; i < n; i++) {
            m[lac[i]] = lbc[i];
        }

        for (int i = 0; i < n; i++) {
            cout << m[la[i]] << endl;
        }

        cout << endl;
    }
    return 0;
}