#include <bits/stdc++.h>
using namespace std;

string solve(int N, const vector<int>& output) {
    stack<int> station;
    int current = 1;
    bool possible = true;

    for (int i = 0; i < N; i++) {
        int desirable_rail = output[i];

        while ((station.empty() || station.top() != desirable_rail) && (current <= N)) {
            station.push(current);
            current++;
        }

        if (station.empty() || station.top() != desirable_rail) {
            possible = false;
            break;
        }
        station.pop();
    }

    return possible ? "Yes" : "No";
}

int main() {
    while (true) {
        int N;
        cin >> N;
        if (N == 0) break;

        while (true) {
            vector<int> output(N);
            cin >> output[0];

            if (output[0] == 0) {
                cout << "\n";
                break;
            }

            for (int i = 1; i < N; ++i) cin >> output[i];
            cout << solve(N, output) << endl;
        }
    }

    return 0;
}
