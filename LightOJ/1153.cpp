#include <bits/stdc++.h>
using namespace std;
const int INF = numeric_limits<int>::max();

int bfs(int s, int t,
        vector<int>& parent,
        vector<vector<int>>& capacity,
        vector<vector<int>>& adj){
    fill(parent.begin(), parent.end(), -1);
    parent[s] = -2;
    queue<pair<int, int>> q;
    q.push({s, INF});

    while (!q.empty()) {
        int cur = q.front().first;
        int flow = q.front().second;
        q.pop();

        for (int next : adj[cur]) {
            if (parent[next] == -1 && capacity[cur][next]) {
                parent[next] = cur;
                int new_flow = min(flow, capacity[cur][next]);
                if (next == t)
                    return new_flow;
                q.push({next, new_flow});
            }
        }
    }

    return 0;
}

int maxflow(int n, int s, int t,vector<vector<int>>& capacity,vector<vector<int>>& adj ){
    int flow = 0;
    vector<int> parent(n);
    int new_flow;

    while ((new_flow = bfs(s, t, parent, capacity, adj))) {
        flow+=new_flow;
        int cur=t;
        while(cur != s){
            int prev = parent[cur];
            capacity[prev][cur] -=new_flow;
            capacity[cur][prev]+=new_flow;
            cur=prev;
        }
    }
    return flow;
}

int main(){
    int T;
    cin >> T;
    int i = 1;
    while(T--){
        int n;
        cin >> n;
        int s; int t; int c;
        cin >> s >> t >> c;
        s--;
        t--;
        vector<vector<int>> capacity(n, vector<int>(n, 0));
        vector<vector<int>> adj(n);
        while(c--){
            int u; int v; int bw; 
            cin >> u >> v >> bw;
            u--;
            v--;
            capacity[u][v] += bw;
            capacity[v][u] += bw;
            adj[u].push_back(v);
            adj[v].push_back(u);
        }

        int flow = maxflow(n,s,t,capacity, adj);
        cout << "Case " << i << ": " << flow << endl;
        i++;

    }


    return 0;
}