#include <bits/stdc++.h>

using namespace std;

int main(){
    string sequence;
    cin >> sequence;
    
    if (sequence.size() == 0){
        cout << 0 << "\n";
        return 0;
    
    }

    int acc = 1;
    int acc_max = 1;
    char c = sequence[0];

    for(int i=1; i < sequence.size(); ++i){
        if (sequence[i]!=c){
            acc_max = max(acc_max,acc);
            acc = 1;
            c = sequence[i];

        }else{
            acc++;
        }

    }
    acc_max = max(acc_max, acc);
    cout << acc_max << "\n";

}

