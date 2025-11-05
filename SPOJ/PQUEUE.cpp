#include <bits/stdc++.h>
using namespace std;

int solve(queue<pair<int,int>> q, int pos){
    int minutes = 0;

    while (!q.empty()) {
        int priority = q.front().first;
        int priority_pos = q.front().second;
        q.pop();

        bool has_upper = false;
        queue<pair<int,int>> aux = q;
        while(!aux.empty()){
            if (aux.front().first > priority){
                has_upper=true;
                break;
            }
            aux.pop();
        }

        if(has_upper){
            q.push({priority, priority_pos});

        } else{
            minutes++;
            if (priority_pos == pos){
                break;
            }

        }

    }

    return minutes;
}

int main() {
    int T;
    cin >> T;
    while(T--){
        int n;
        int m;
        // n: num trabajos en cola, posición de mi trabajo
        cin >> n >> m;
        int x;
        // cola de trabajos {prioridad, posición}
        queue<pair<int,int>> q;
        for (int i=0; i<n;i++){
            cin >> x;
            q.push({x, i});
        }

        cout << solve(q,m) << endl;
    }


return 0;
}