#include <bits/stdc++.h>
using namespace std;

int solve(vector<int> &weights, vector<int> &values, int capacity){
    int n = weights.size();
    vector<vector<int>> dp(n+1, vector<int>(capacity+1, 0));

    for (int i=1; i<n+1; i++){
        for (int w=0; w<capacity+1;w++){
            if (weights[i-1] > w){
                dp[i][w] = dp[i-1][w];
            } else{
                dp[i][w] = max(
                    dp[i-1][w],
                    values[i-1] + dp[i-1][w-weights[i-1]]
                );
            }
        }
    }

    return dp[n][capacity];
}

int main(){
    int n; int x;
    cin >> n >> x;
    vector<int> prices(n);
    vector<int> pages(n);
    for (int i=0; i<n; i++){
        int h;
        cin >> h;
        prices[i]=h;
    }
    for (int i=0; i<n; i++){
        int s;
        cin >> s;
        pages[i]=s;
    }

    int res = solve(prices, pages, x);
    cout << res << endl;

}
