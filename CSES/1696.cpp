#include <bits/stdc++.h>
using namespace std;

using ll = long long;
const ll INF = LLONG_MAX;

// BFS para encontrar un camino aumentante
ll bfs(int s, int t, vector<int>& parent, vector<vector<ll>>& cap, vector<vector<int>>& adj) {
    fill(parent.begin(), parent.end(), -1);
    parent[s] = -2;
    queue<pair<int,ll>> q;
    q.push({s, INF});
    while(!q.empty()){
        int cur = q.front().first;
        ll flow = q.front().second;
        q.pop();
        for(int nxt : adj[cur]){
            if(parent[nxt] == -1 && cap[cur][nxt] > 0){
                parent[nxt] = cur;
                ll new_flow = min(flow, cap[cur][nxt]);
                if(nxt == t) return new_flow;
                q.push({nxt, new_flow});
            }
        }
    }
    return 0;
}

// Edmonds-Karp / Max Flow
ll maxflow(int n, int s, int t, vector<vector<ll>>& cap, vector<vector<int>>& adj){
    ll flow = 0;
    vector<int> parent(n);
    ll new_flow;
    while((new_flow = bfs(s,t,parent,cap,adj))){
        flow += new_flow;
        int cur = t;
        while(cur != s){
            int prev = parent[cur];
            cap[prev][cur] -= new_flow;
            cap[cur][prev] += new_flow;
            cur = prev;
        }
    }
    return flow;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n,m,k;
    cin >> n >> m >> k;

    int V = n + m + 2;
    int source = 0, sink = V-1;

    vector<vector<ll>> cap(V, vector<ll>(V,0));
    vector<vector<int>> adj(V);

    auto add_edge = [&](int u, int v, ll c){
        cap[u][v] += c;
        adj[u].push_back(v);
        adj[v].push_back(u); // residual
    };

    // source -> boys
    for(int i=1;i<=n;i++) add_edge(source,i,1);
    // girls -> sink
    for(int i=1;i<=m;i++) add_edge(n+i,sink,1);

    // leer potenciales parejas
    for(int i=0;i<k;i++){
        int a,b;
        cin >> a >> b;
        add_edge(a,n+b,1);
    }

    ll flow = maxflow(V, source, sink, cap, adj);
    cout << flow << endl;

    vector<int> match_boy(n+1,0);
    for(int boy=1; boy<=n; boy++){
        for(int girl : adj[boy]){
            if(girl >= n+1 && girl <= n+m && cap[girl][boy] > 0){
                match_boy[boy] = girl - n;
                break;
            }
        }
    }

    for(int boy=1; boy<=n; boy++){
        if(match_boy[boy]) cout << boy << " " << match_boy[boy] << endl;
    }

    return 0;
}