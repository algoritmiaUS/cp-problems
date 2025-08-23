#include <bits/stdc++.h>
 
using namespace std;
 
int main() {
    int t;
    cin >> t;
    
    while (t--) {
        long long n;
        cin >> n;
        
        long long mod = 11;
        vector <long long> ans;
        while (n >= mod) {
            if (n % mod == 0)
                ans.push_back(n / mod);
            mod = (mod - 1) * 10 + 1;
        }
        
        cout << (int)ans.size() << '\n';
        for (int i = (int)ans.size() - 1; i >= 0; --i)
            cout << ans[i] << ' ';
        if(ans.size()) cout << '\n';
    }
    
    return 0;
}