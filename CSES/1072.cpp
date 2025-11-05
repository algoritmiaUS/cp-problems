#include <bits/stdc++.h>

using namespace std;

long generate_ways(long k){
    long total_ways = (k*k*(k*k-1)) /2;
    long attacking_ways = 4 * (k-1) * (k-2);
    long res = total_ways -  attacking_ways;
    return res;
}


int main(){
    int n;
    cin >> n;

    for(int k = 1; k<=n;k++){
        cout << generate_ways(k) << endl;
    }


    return 0;
}