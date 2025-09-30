#include <bits/stdc++.h>
using namespace std;
typedef long long ll;


int main(){
    int m; int n;
    cin >> m >> n;
    map<string,int> map;
    while(m--){
        string job; int value;
        cin >> job >> value;
        map.insert({job, value});
    }

    while(n--){
        ll res = 0;
        string w;
        while(cin >> w && w!="."){
            if(map.count(w)){
                res+=map[w];
            }
        }

        cout << res << endl;
    }

    return 0;
}