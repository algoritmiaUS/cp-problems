#include <bits/stdc++.h>
using namespace std;

void dfs(vector<vector<int>> &adj, vector<bool> &visited, int v, vector<int> &comp){
    visited[v] = true;
    comp.push_back(v);
    for(int u: adj[v]){
        if (!visited[u]) dfs(adj, visited, u, comp); 
    }

}

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
    vector<bool> visited(n+1, false);
    vector<vector<int>> comp_v;
    for (int v = 1; v <= n; ++v) {
        if (!visited[v]){
            vector<int> comp;
            dfs(adj, visited, v, comp);
            comp_v.push_back(comp);  

        }
    }    

    cout << comp_v.size()-1 << endl;

    for (int i=0; i<comp_v.size()-1; i++){
        cout << comp_v[i][0] << " " <<comp_v[i+1][0] << endl;
    }

    return 0;
}
