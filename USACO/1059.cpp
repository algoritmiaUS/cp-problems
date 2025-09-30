// Problem: Do You Know Your ABCs?
// Solution by Kenny Jesús Flores Huamán
// url: https://usaco.org/index.php?page=viewproblem2&cpid=1059


#include <string>
#include <bits/stdc++.h>
using namespace std;

int main(){
    int n=7;
    vector<int> v(7);
    for(int i = 0; i < n; i++) cin >> v[i];
    sort(v.begin(), v.end());
    int a = v[0];//a
    int abc = v.back(); //a+b+c
    int bc = abc-a; // b+c

    // buscamos a+b y a+c
    vector<int> temp(2);
    int count=0;
    for(int i = 1; i < v.size(); i++){
        if (std::find(v.begin(), v.end(), abs(v[i]-a)) != v.end()) {
            temp[count]= v[i]-a;
            count++;
        }
    }

    int b = *min_element(temp.begin(), temp.end());
    int c = *max_element(temp.begin(), temp.end());
    cout << a << " " << b << " " << c << endl; 
    return 0;
}