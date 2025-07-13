#include <bits/stdc++.h>

using namespace std;

int main(){
    int t;
    cin >> t;

    while(t--){
        long long r;
        long long c;
        cin >> r >> c;
        

        if (r==c){
           cout << r * r - (r-1) << "\n";
        } else{
            long long val = max(r,c);
            val =  val * val - (val -1);

            if (c > r){
                if (c%2 == 0){
                    val -= (c-r);
                } else{
                    val += (c-r);
                }
            } else if (r>c){
                if (r%2 == 0){
                    val += (r-c);
                } else{
                    val -= (r-c);
                }

            }
            cout << val << "\n";

        } 

    }



    return 0;
}