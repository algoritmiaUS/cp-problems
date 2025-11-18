#include <bits/stdc++.h>
using namespace std;
unordered_map<string, int> m;

int main(){
    int n;
    cin >>n;
    string s;
    while(n--){
        cin >> s;
        if(m.count(s)==0){
            m[s]=1;
            cout << "OK" << endl;
        } else{
            cout << s << m[s] << endl;
            m[s]+=1;
        }
    }

    return 0;
}