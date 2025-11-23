#include <bits/stdc++.h>
using namespace std;

// Realizado: ordenando una lista y ordenando O(n log(n))
// int main(){
//     int n;
//     cin >> n;
//     vector<int> v(n);
//     int x;
//     for(int i=0; i<n; i++){
//         cin >> x;
//         v[i]=x;
//     }
//     sort(v.begin(), v.end());
//     int acc = 1;
//     for(int i=1; i<n; i++){
//         acc += (v[i] != v[i-1]);
//     }
//     cout << acc << endl;
//     return 0;

// }

// Realizado haciendo uso de set O(n)
// Sorted set da problemas en este ejercicio
int main(){
    int n;
    cin >>n;
    set<int> s;
    int x;
    for(int i=0; i<n; i++){
        cin >> x;
        s.insert(x);
    }

    cout << s.size() << endl;

    return 0;
}