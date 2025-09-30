// Problem: Word Processor
// Solution by Kenny Jesús Flores Huamán
// url: https://usaco.org/index.php?page=viewproblem2&cpid=987

#include <string>
#include <bits/stdc++.h>
using namespace std;

int main(){
    ifstream fin("word.in");
    ofstream fout("word.out");

    int n; int k;
    fin >> n >> k;
    vector<string> words(n);
    for(int i = 0; i < n; i++) fin >> words[i];

    vector<string> temp;
    int current_len = 0;
    for(string x : words){
        if (current_len ==0){
            // first element
            temp.push_back(x);
            current_len += x.size();
        } else{

            if (current_len + x.size() <= k){
                temp.push_back(x);
                current_len+= x.size();

            } else{
                string t = "";
                for(int i=0; i<temp.size(); i++){
                    t += temp[i];
                    if (i != temp.size()-1) t += " ";
                }
                fout << t << endl;
                temp.clear();
                temp.push_back(x);
                current_len = x.size();
            }
        }

        
    }

    if (!temp.empty()){
    string t = "";
    for(int i=0; i<temp.size(); i++){
        t += temp[i];
        if (i != temp.size()-1) t += " ";
    }
    fout << t << endl;
    }

    fin.close();
    fout.close();
    return 0;
}