#include <bits/stdc++.h>
using namespace std;

void load_team_definitions(int num_teams, map<int, int>& element_to_team_map, map<int, queue<int>>& team_queues) {
    for (int team_id = 1; team_id <= num_teams; ++team_id) {
        team_queues[team_id] = queue<int>();

        int num_elems;
        int elem;
        cin >> num_elems;
        
        for (int j = 0; j < num_elems; ++j) {
            cin >> elem;
            element_to_team_map[elem] = team_id;
        }
    }
}

void handle_enqueue(int member_id, map<int, int>& element_to_team_map, map<int, queue<int>>& team_queues, queue<int>& principal_q, unordered_set<int>& active_teams) {
    int team_id = element_to_team_map[member_id];

    if (active_teams.find(team_id) == active_teams.end()) {
        active_teams.insert(team_id);
        principal_q.push(team_id);
    }

    team_queues[team_id].push(member_id);
}

void handle_dequeue(map<int, queue<int>>& team_queues, queue<int>& principal_q, unordered_set<int>& active_teams) {
    int team_id = principal_q.front();

    int dequeued_element = team_queues[team_id].front();
    team_queues[team_id].pop();

    cout << dequeued_element << endl;

    if (team_queues[team_id].empty()) {
        active_teams.erase(team_id);
        principal_q.pop();
    }
}

void process_commands(map<int, int>& element_to_team_map, map<int, queue<int>>& team_queues, queue<int>& principal_q, unordered_set<int>& active_teams) {
    string command;
    while (cin >> command && command != "STOP") {
        if (command == "ENQUEUE") {
            int member_id;
            cin >> member_id;
            handle_enqueue(member_id, element_to_team_map, team_queues, principal_q, active_teams);
        } else if (command == "DEQUEUE") {
            handle_dequeue(team_queues, principal_q, active_teams);
        }
    }
}

void solve(int scenario_num, int num_teams) {
    // Mapeo: Elemento ID -> Equipo ID
    map<int, int> element_to_team_map; 
    // Colas internas: Equipo ID -> Cola de Elementos
    map<int, queue<int>> team_queues; 
    // Cola Principal: Orden de llegada de los EQUIPOS
    queue<int> principal_q;
    // Set de Control: Equipos con miembros esperando
    unordered_set<int> active_teams;

    load_team_definitions(num_teams, element_to_team_map, team_queues);

    cout << "Scenario #" << scenario_num << endl;

    process_commands(element_to_team_map, team_queues, principal_q, active_teams);

    cout << endl;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int num_teams;
    int scenario_counter = 0;

    while ((cin >> num_teams) && num_teams != 0) {
        scenario_counter++;
        solve(scenario_counter, num_teams);
    }

    return 0;
}