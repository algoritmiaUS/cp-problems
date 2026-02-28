#include <bits/stdc++.h>
using namespace std;

using ll = long long;

const ll INF = numeric_limits<ll>::max();

ll bfs(int s, int t,
       vector<int>& parent,
       vector<vector<ll>>& capacity,
       vector<vector<int>>& adj) {
    
    fill(parent.begin(), parent.end(), -1);
    parent[s] = -2;

    queue<pair<int, ll>> q;
    q.push({s, INF});

    while (!q.empty()) {
        int cur = q.front().first;
        ll flow = q.front().second;
        q.pop();

        for (int next : adj[cur]) {
            if (parent[next] == -1 && capacity[cur][next] > 0) {
                parent[next] = cur;
                ll new_flow = min(flow, capacity[cur][next]);
                if (next == t)
                    return new_flow;
                q.push({next, new_flow});
            }
        }
    }

    return 0LL;
}

ll maxflow(int n, int s, int t,
           vector<vector<ll>>& capacity,
           vector<vector<int>>& adj) {
    
    ll flow = 0;
    vector<int> parent(n);
    ll new_flow;

    while ((new_flow = bfs(s, t, parent, capacity, adj))) {
        flow += new_flow;
        int cur = t;

        while (cur != s) {
            int prev = parent[cur];
            capacity[prev][cur] -= new_flow;
            capacity[cur][prev] += new_flow;
            cur = prev;
        }
    }

    return flow;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;

    int V = n;
    int source = 0;
    int sink = V - 1;

    vector<vector<ll>> capacity(V, vector<ll>(V, 0));
    vector<vector<int>> adj(V);

    auto add_edge = [&](int u, int v, ll cap) {
        capacity[u][v] += cap;
        adj[u].push_back(v);
        adj[v].push_back(u); // residual
    };

    while (m--) {
        int a, b;
        ll c;
        cin >> a >> b >> c;
        a--;
        b--;
        add_edge(a, b, c);
    }

    ll flow = maxflow(V, source, sink, capacity, adj);
    cout << flow << endl;

    return 0;
}