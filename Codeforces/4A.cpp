// Problem: Watermelon
// Solution by Kenny Jesús Flores Huamán
// url: https://codeforces.com/problemset/problem/4/A

#include <bits/stdc++.h>
using namespace std;

int main(){
    int w;
    cin >> w;

    if(w%2==1 or w==2){
        cout << "NO" << endl;
    } else{
        cout << "YES" << endl;
    }

    return 0;
}