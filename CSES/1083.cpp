#include <bits/stdc++.h>

using namespace std;

int main(){
    int n;
    cin >> n;
    vector<int> v(n-1);
    for(int i = 0; i < v.size(); ++i){
        cin >> v[i];
    }
    sort(v.begin(), v.end());

    for (int i = 0; i < v.size(); ++i) {
        if(v[i] != i+ 1){
            cout << i+1 << "\n";
            return 0;
        }

    }

    cout << n << "\n";

}

