// Problem: DNA Prefix
// Solution by Kenny Jesús Flores Huamán
// url: https://lightoj.com/problem/dna-prefix

import java.io.BufferedReader
import java.io.InputStreamReader

class TrieNode{
    val children : MutableMap<Char, TrieNode> = mutableMapOf()
    var count: Int = 0
}

class Trie{
    private val root : TrieNode = TrieNode()

    fun insert(word:String){
        var current = root
        for (char in word){
            current = current.children.getOrPut(char) {TrieNode()}
            current.count +=1
        }
    }

    fun findMaxPrefixScore(): Int {
        var max_score = 0

        fun dfs(node: TrieNode, depth: Int) {
            max_score = maxOf(max_score, depth * node.count)
            for (child in node.children.values) {
                dfs(child, depth + 1)
            }
        }

        dfs(root, 0)
        return max_score
    }



}


fun main() {
    val reader = BufferedReader(InputStreamReader(System.`in`))
    val numTests = reader.readLine().toInt() // Número de casos de prueba

    val results = StringBuilder()
    for (t in 1..numTests) {
        val trie = Trie()
        val n = reader.readLine().toInt()

        repeat(n) {
            val adn = reader.readLine()
            trie.insert(adn)
        }

        val res = trie.findMaxPrefixScore()
        results.append("Case $t: $res\n")
    }

    print(results)
}