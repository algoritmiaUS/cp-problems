#include <bits/stdc++.h>

using namespace std;

int main(){
    int t, n, m;
    string a, b, c;
    // string a remains the same
    cin >> t;
    while(t--){
        cin >> n >> a >> m >> b >> c;

        for(int i = 0; i < m; i++){
            if(c[i] == 'D') a += b[i];
            else a = b[i] + a;
        }
    
        cout << a << endl;
    }

}