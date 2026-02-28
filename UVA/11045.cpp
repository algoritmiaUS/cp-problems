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

int maxflow(int n, int s, int t,
    vector<vector<int>>& capacity,
    vector<vector<int>>& adj){
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

map<string,int> m = {
    {"XS",0},
    {"S",1},
    {"M",2},
    {"L",3},
    {"XL",4},
    {"XXL",5}
};

int main(){
    int T;
    cin >> T;
    while(T--){
        int N; int M;
        cin >> N >> M;
        int tshirts_per_size = N / 6;

        int V = 6 + M + 2;
        int source = 0;
        int sink = V-1;

        vector<vector<int>> capacity(V, vector<int>(V, 0));
        vector<vector<int>> adj(V);

        auto add_edge = [&](int u, int v, int cap){
            capacity[u][v] += cap;
            adj[u].push_back(v);
            adj[v].push_back(u); // para residual
        };

        // source -> tallas
        for(int i = 0; i < 6; i++){
            int size_node = 1 + i;
            add_edge(source, size_node, tshirts_per_size);
        }

        // tallas → voluntarios
        for(int i = 0; i < M; i++){
            string a, b;
            cin >> a >> b;

            int vol_node = 1 + 6 + i;

            int size1 = 1 + m[a];
            int size2 = 1 + m[b];

            add_edge(size1, vol_node, 1);
            add_edge(size2, vol_node, 1);
        }

        // Members -> sink
        for(int i = 0; i < M; i++){
            int vol_node = 1 + 6 + i;
            add_edge(vol_node, sink, 1);
        }

        int flow = maxflow(V,source,sink,capacity, adj);
        if (flow ==M){
            cout << "YES" << endl;
        } else{
            cout << "NO" << endl;
        }

    }

    return 0;
}