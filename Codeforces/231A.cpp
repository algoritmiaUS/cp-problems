// Problem: Team
// Solution by Kenny Jesús Flores Huamán
// url: https://codeforces.com/problemset/problem/231/A

#include <bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cin >> n;
    int acc = 0;
    while (n--){
        int p;
        int v;
        int t;
        cin >> p >> v >> t;
        if((p+v+t)>=2){
            acc+=1;
        }
    }
    cout << acc << endl;
    return 0;
}