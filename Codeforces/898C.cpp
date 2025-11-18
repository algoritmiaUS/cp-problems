#include <bits/stdc++.h>
using namespace std;

bool isSuffix(const string &a, const string &b) {
    if (b.size() < a.size()) return false;
    return b.compare(b.size() - a.size(), a.size(), a) == 0;
}

int main() {
    int n;
    cin >> n;

    map<string, set<string>> book;

    // Read input and merge numbers per person
    while (n--) {
        string name;
        int k;
        cin >> name >> k;
        while (k--) {
            string phone;
            cin >> phone;
            book[name].insert(phone);  // deduplicate
        }
    }

    cout << book.size() << "\n";

    // Process each person
    for (auto &entry : book) {
        const string &name = entry.first;
        vector<string> phones(entry.second.begin(), entry.second.end());
        int s = phones.size();

        vector<bool> remove_flag(s, false);

        // Detect suffix numbers
        for (int i = 0; i < s; i++) {
            for (int j = 0; j < s; j++) {
                if (i == j) continue;
                if (isSuffix(phones[i], phones[j])) {
                    remove_flag[i] = true;
                }
            }
        }

        // Collect valid phone numbers
        vector<string> accepted;
        for (int i = 0; i < s; i++) {
            if (!remove_flag[i]) accepted.push_back(phones[i]);
        }

        // Output
        cout << name << " " << accepted.size();
        for (auto &num : accepted) cout << " " << num;
        cout << "\n";
    }

    return 0;
}




