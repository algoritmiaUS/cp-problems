#include <bits/stdc++.h>
using namespace std;

typedef long long ll;


int main() {
    int t;
    cin >> t;

    while(t--){
        ll n;
        cin >> n;
        cout << (ll)floor((-1+sqrt(1+(8LL*n)))/2) << endl;
        // El cast es para forzar que el valor siga siendo
        // un long long, y no un double a causa del sqrt
    }

}