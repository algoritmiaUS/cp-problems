#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        int n = cost.size();
        vector<int> dp(n,-1);
        return min(solve(cost, dp, 0), solve(cost, dp, 1));
    }

private:
    int solve(vector<int>& cost, vector<int>& dp, int currentStep){
        if (currentStep >= cost.size()){
            return 0;
        } 

        if(dp[currentStep]!=-1){
            return dp[currentStep];        }

        dp[currentStep] = cost[currentStep] + min(
            solve(cost, dp, currentStep+1),
            solve(cost, dp, currentStep+2)
        );

        return dp[currentStep];
    }
};