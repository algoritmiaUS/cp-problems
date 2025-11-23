#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    int Q;
    cin >> Q;
    map<ll,ll> m;
    int k;
    long long  a;
    long long v;
    
    while (Q--){
        cin >>k;
        if (k==0){
            cin >> a;
            cin >> v;
            m[a]=v;          
        } else{
            cin >> a;
            cout << m[a] << endl;
        }
    }
}