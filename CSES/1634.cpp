#include <bits/stdc++.h>
using namespace std;
#define INF 1000000007

int main(){
    int n, x;
    cin >> n >> x;
    vector<int> coins(n);
    for(int i = 0; i < n; i++){
        cin >> coins[i];
    }

    vector<int> dp(x + 1, INF);
    dp[0] = 0;

    for(int w = 1; w <= x; w++){
        for(int i = 0; i < n; i++){  
            if(coins[i] <= w){
                dp[w] = min(dp[w], 1 + dp[w - coins[i]]); 
            }
        }
    }

    int res = (dp[x] != INF) ? dp[x] : -1;
    cout << res << endl;
    return 0;
}
