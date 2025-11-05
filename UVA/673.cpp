#include <bits/stdc++.h>
using namespace std;

string solve(string s) {
    stack<char> st;
    for (char c : s) {
        if (c == '(' || c == '[') {
            st.push(c);
        } else if (c == ')' || c == ']') {
            if (st.empty()) return "No";
            if ((c == ')' && st.top() == '(') || (c == ']' && st.top() == '[')) {
                st.pop();
            } else {
                return "No";
            }
        } 
    }
    return st.empty() ? "Yes" : "No";
}

int main() {
    int n;
    cin >> n;
    cin.ignore();

    while (n--) {
        string line;
        getline(cin, line);
        cout << solve(line) << '\n';
    }
}