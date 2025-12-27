#include <bits/stdc++.h>
using namespace std;

int solve(string n){
    while (n.size() < 4) {
        n = "0" + n;
    }
    int acc = 0;
    if (n == "6174") return 0;
    if(n.find_first_not_of(n[0]) == string::npos) return 8;
    vector<int> v(4);
    for (int i = 0; i < 4; i++) {
        v[i] = n[i] - '0';
    }


    for (int i =1; i<=7; i++){
        acc++;
        vector<int> v1 = v;
        vector<int> v2 = v;
        sort(v1.begin(), v1.end());
        sort(v2.begin(), v2.end(), greater<int>());
        int a = v1[0]*1000 + v1[1]*100 + v1[2]*10 + v1[3];
        int b = v2[0]*1000 + v2[1]*100 + v2[2]*10 + v2[3];
        int diff = b - a;
        for (int j = 3; j >= 0; j--) {
            v[j] = diff % 10;
            diff /= 10;
        }

        if (v[0]==6 && v[1]==1 && v[2]==7 && v[3]==4) {
            break;
        }


    }
    return acc;
}


int main(){
    int t;
    cin >> t;
    string n;
    while(t--){
        cin >> n;
        cout << solve(n) << endl;
    }


    return 0;
}