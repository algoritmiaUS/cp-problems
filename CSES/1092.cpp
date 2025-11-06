#include <bits/stdc++.h>

using namespace std;

int main(){
    int n;
    cin >> n;

    long long acc = (long long)n * (n + 1) / 2;

    if (acc %2 !=0){
        cout << "NO" << endl;
    } else{
        long long T = acc /2;
        long long current_sum = 0;
        vector<int> fst_v;
        vector<int> snd_v;

        for (int i = n; i >= 1; i--) {
            if (current_sum + i <= T) {
                current_sum += i;
                fst_v.push_back(i);
            } else{
                snd_v.push_back(i);
            }
        }

        cout << "YES" << endl;
        cout << fst_v.size() << endl;
        for (int i : fst_v){
            cout << i << " ";
        }
        cout <<"\n";
        cout << snd_v.size() << endl;
        for (int i : snd_v){
            cout << i << " ";
        }
        cout <<"\n";
    }
    return 0;
}