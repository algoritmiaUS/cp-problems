// Versión Bottom-up
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> vv(numRows);
        vv[0] = {1};
        
        if (numRows >1){
            vv[1]= {1,1};
        }

        for(int i=3; i<=numRows; i++){
            vector<int> acc(i);
            acc[0] = 1;
            acc[i - 1] = 1;
            for(int j=1; j < i - 1; j++){
                acc[j] = vv[i - 2][j - 1] + vv[i - 2][j];
            }
            vv[i-1] = acc;

        }
       return vv;
    }
};