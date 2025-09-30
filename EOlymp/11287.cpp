#include <bits/stdc++.h>
using namespace std;

int search(vector<int> v){
    int left = 0;
    int right = v.size() - 1;

    while (left < right){
        int mid =  left + (right - left) /2;

        if (v[mid] < v[mid+1]){
            left = mid+1;
        } else{
            right = mid;
        }


    }
    return left;
}

int main() {
    int n;
    cin >> n;
    vector<int> v(n);
    int x;
    for (int i=0; i<n ; ++i){
        cin >> x;
        v[i]= x;
    }
    int idx = search(v);

    cout << idx << endl;

}