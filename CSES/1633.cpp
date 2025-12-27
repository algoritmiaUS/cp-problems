#include <bits/stdc++.h>

using namespace std;
const int MOD = 1000000007;

int solve(int n){
    vector<int> dp(n+1,0);
    dp[0]=1;

    for (int i=1; i<n+1; i++){
        for (int j=1; j<7;j++){
            if(i-j>=0){
                dp[i] = (dp[i] + dp[i-j]) % MOD;
            }
        }
    }

    return dp[n];
}

int main(){
    int n; cin >> n;
    cout << solve(n) << endl;
}
