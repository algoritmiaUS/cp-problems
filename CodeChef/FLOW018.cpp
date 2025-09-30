#include <bits/stdc++.h>
using namespace std;

long factorial(int n){
    if (n<1) return 1;
    return n * factorial(n-1);
}

int main() {

    int t;
    cin >> t;
    long x;
    while(t--){
        cin >> x;
        long res;
        res = factorial(x);
        cout << res << endl;
    }
}