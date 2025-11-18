#include <bits/stdc++.h>
using namespace std;
typedef vector<int> vi;

void dfs(vector<vector<int>> &adj, vector<bool> &visited, vector<bool> &isopen, int v){
    visited[v] = true;
    for(int u : adj[v]){
        if (!visited[u] && !isopen[u]){
            dfs(adj, visited, isopen, u);
        } 
    }
}

bool alltrue(vector<bool>& v){
    return all_of(v.begin() + 1, v.end(), [](bool x){ return x; });
}

int main(){
    ifstream fin("closing.in");
    ofstream fout("closing.out");
    int n;
    int m;
    fin >> n >> m;
    vector<vi> adj(n+1);
    for (int i = 0; i < m; i++){
        int u;
        int v;
        fin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    vector<bool> isopen(n+1, false);
    vector<bool> visited(n+1, false);
    int start = 1;
    dfs(adj, visited, isopen, start);
    fout << (alltrue(visited) ? "YES" : "NO") << endl;
    int remaining = n - 1;
    while (remaining--) {
        int v;
        fin >> v;
        isopen[v] = true;  
        fill(visited.begin(), visited.end(), false);
        for (int j = 1; j <= n; j++)
        if (isopen[j]) visited[j] = true;
        int start = -1;
        for (int j = 1; j <= n; j++) {
            if (!isopen[j]) {
                start = j;
                break;
            }
        }

        if (start != -1) dfs(adj, visited, isopen, start);
        fout << (alltrue(visited) ? "YES" : "NO") << endl;


    }
    
    return 0;
}