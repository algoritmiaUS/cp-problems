#include <iostream>
#include <vector>
#include <cstdint>

using namespace std;

void print_passwords(const string& rule, size_t rule_index, const vector<string>& words, string line) {
    if (rule_index == rule.size()) {
        cout << line << endl;
        return;
    }

    char c = rule[rule_index];
    if (c == '#') {
        for (const string& word : words) {
            print_passwords(rule, rule_index + 1, words, line + word);
        }
    } else if (c == '0') {
        for (uint16_t j = 0; j < 10; j++) {
            print_passwords(rule, rule_index + 1, words, line + to_string(j));
        }
    }
}

int main() {
    size_t n;
    while (cin >> n) {
        vector<string> words;
        for (size_t i = 0; i < n; i++) {
            string word;
            cin >> word;
            words.push_back(word);
        }

        size_t m;
        cin >> m;
        vector<string> rules;
        for (size_t i = 0; i < m; i++) {
            string rule;
            cin >> rule;
            rules.push_back(rule);
        }

        cout << "--" << endl;
        for (const string& rule : rules) {
            print_passwords(rule, 0, words, "");
        }
    }

    return 0;
}