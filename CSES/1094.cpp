// Problem: Increasing Array
// URL:https://cses.fi/problemset/task/1068


#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<long int> v(n);
    for (int i = 0; i < v.size(); ++i) {
        cin >> v[i];
    }
    long long moves = 0;
    for (int i = 1; i < v.size(); ++i) {
        if (v[i] < v[i - 1]) {
            moves += v[i - 1] - v[i];
            v[i] = v[i - 1]; // actualiza el valor para mantener el orden creciente
        }
    }
    cout << moves << "\n";
}
