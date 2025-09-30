// Problem: Promotion Counting
// Solution by Kenny Jesús Flores Huamán
// url: https://usaco.org/index.php?page=viewproblem2&cpid=591

#include <string>
#include <bits/stdc++.h>
using namespace std;

int main(){
    ifstream fin("promote.in");
    ofstream fout("promote.out");

    int br_1; int br_2;
    int silv_1; int silv_2;
    int gld_1; int gld_2;
    int pl_1; int pl_2;

    fin >> br_1 >> br_2;
    fin >> silv_1 >> silv_2;
    fin >> gld_1 >> gld_2;
    fin >> pl_1 >> pl_2;

    int gold_to_pl = pl_2 - pl_1;
    int silv_to_gld = (gld_2 -  gld_1) +  gold_to_pl;
    int bronze_to_slv = (silv_2 - silv_1) +  silv_to_gld;

    fout << bronze_to_slv << endl;
    fout << silv_to_gld << endl;
    fout << gold_to_pl << endl;


    fin.close();
    fout.close();
    return 0;
}
