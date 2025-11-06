
#include <bits/stdc++.h>

using namespace std;
int main(){


    long long n;
    cin >> n;

    long long res = 0;
    long long mult = 5;

    while (n / mult > 0) {
        res += n / mult;
        mult *= 5;
    }   
    cout << res << endl;

    return 0;
}
