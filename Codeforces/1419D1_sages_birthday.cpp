// Solution by Inés Dávila Herrero.
// URL: https://codeforces.com/problemset/problem/1419/D1

#include <bits/stdc++.h>

using namespace std;

int main(){
    int n;
    cin >> n;

    vector<int> list(n);
    for(int i=0; i<n; i++){
        cin >> list[i];
    }
    sort(list.begin(), list.end());
    
    int r = n / 2;
    if(n % 2 == 0){
        r--;
    }

    cout << r << endl;

    for(int i=0; i<n/2; i++){
        cout << list[i + n/2] << ' ' << list[i] << ' ';
    }

    if(n % 2 == 1){
        cout << list[n - 1];
    }
}
