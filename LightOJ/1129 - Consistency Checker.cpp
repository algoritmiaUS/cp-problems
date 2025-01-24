#include <iostream>
#include <limits>
#include <map>
#include <vector>

using namespace std;

template <typename T>
class trie {
private:
    map<T, trie<T>> content;

public:
    // Must implement an iterator const &T
    template <typename C>
    bool insert(C& collection) {
        bool is_prefix_of_or_from = true;
        map<T, trie<T>>* current_node = &content;
        for (auto it = collection.cbegin(); it != collection.cend(); it++) {
            auto next_node = current_node->find(*it);
            if (next_node == current_node->end()) {
                is_prefix_of_or_from = current_node->empty();
                for (; it != collection.cend(); it++) {
                    (*current_node)[*it] = trie();
                    current_node = &(*current_node)[*it].content;
                }

                break;
            }

            current_node = &next_node->second.content;
        }

        return is_prefix_of_or_from;
    }

};

int main() {
    size_t t = 0;
    cin >> t;

    for (size_t i = 0; i < t; i++) {
        size_t n = 0;
        cin >> n;

        trie<char> words;
        bool prefix_exists = false;
        for (size_t j = 0; j < n; j++) {
            string number;
            cin >> number;
            if (j == 0) {
                words.insert(number);
                continue;
            }

            if (prefix_exists = words.insert(number)) {
                for (; j < n; j++) {
                    cin.ignore(numeric_limits<streamsize>::max(), '\n');
                }

                break;
            }
        }

        cout << "Case " << i + 1 << ": " << (prefix_exists ? "NO" : "YES") << endl;
    }

    return 0;
}