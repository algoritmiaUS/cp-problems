#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    unordered_map<int,int> m;

    Solution() {
        m[0] = 0;
        m[1] = 1;
        m[2] = 1;
    }
    int tribonacci(int n) {
        if (m.count(n)){
            return m[n];
        }

        m[n] = tribonacci(n-1) 
                    + tribonacci(n-2) 
                    + tribonacci(n-3);
        return m[n];
    }
};