#include <bits/stdc++.h>
using namespace std;
#define MOD 1000000007

int main(){
    int n;
    int x;
    cin >> n >> x;
    vector<int> coins(n);
    for (int i=0; i<n; i++){
        int c;
        cin >> c;
        coins[i]=c;
    }

    vector<int> dp(x+1,0);
    dp[0]=1; // solo existe 1 forma de conseguir 0, no usar ninguna moneda

    for (int c: coins){
        for(int i=c; i<=x; i++){
            dp[i] = (dp[i] + dp[i - c]) % MOD;
        }
    }

    cout << dp[x] << endl;


    return 0;
}
