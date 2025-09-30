// Problem: Soldier and Bananas
// Solution by Kenny Jesús Flores Huamán
// url: https://codeforces.com/problemset/problem/546/A

#include <bits/stdc++.h>
using namespace std;

int main(){
    int k; int n; int w;
    cin >> k >> n >> w;
    int acc = 0;
    for (int i=1; i<=w; i++){
        acc += k*i;
    }

    if(acc <= n){
        cout << 0 << endl;
    } else{
        cout << (acc-n) << endl;
    }
    return 0;
}
