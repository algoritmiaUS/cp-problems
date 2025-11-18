#include <bits/stdc++.h>
using namespace std;



int main(){
    int n;
    int m;
    cin >> n >> m;
    vector<vector<int>> adj(n+1);
    while (m--) {
        int node;
        int vertex;
        cin >> node >> vertex;
        adj[node].push_back(vertex);
        adj[vertex].push_back(node);
    }
    vector<int> colored(n+1, -1);
    vector<vector<int>> comp_v;
    queue<int> q;
    for (int i = 1; i <= n; i++) {
        if (colored[i] == -1){
            colored[i]=0;
            q.push(i);
            while(!q.empty()){
                int u = q.front();
                q.pop();

                for (auto &v : adj[u]){
                    if (colored[v]==-1){
                        colored[v] = 1- colored[u];
                        q.push(v);
                    } else if(colored[v] == colored[u]){
                        cout << "IMPOSSIBLE\n";
                        return 0;
                    }
                }
            }

        }
    }    

    for (int v = 1; v <= n; v++)
        cout << colored[v] + 1 << " ";
    cout << "\n";
    return 0;
}
