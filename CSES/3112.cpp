
#include <bits/stdc++.h>
using namespace std;

int main(){

    int left = 1;
    int right = 1e9;

    while (left < right){
        int mid = left+(right-left)/2;
        cout << "? " << mid << endl;
        string response;
        cin >> response;
        if (response == "YES"){
            left = mid+1;
        } else{
            right = mid;
        }
    }

    cout << "! " << left << endl;

}