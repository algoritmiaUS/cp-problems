#include <bits/stdc++.h>
using namespace std;

string superDigit(string p){
    if (p.size() ==1) return p;

    long long  res = 0;
    for (char c : p){
        res+= (c - '0');
    }
    return superDigit(to_string(res));

}

int main() {
    string n;
    long long k;
    cin >> n >> k;

    long long sumDigits = 0;
    for (char c : n) {
        sumDigits += (c - '0');
    }

    long long initial = sumDigits * k;

    string res = superDigit(to_string(initial));
    cout << res << endl;
}