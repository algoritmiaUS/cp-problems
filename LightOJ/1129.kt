// Problem: Consistency Checker
// Solution by Kenny Jesús Flores Huamán
// url: https://lightoj.com/problem/consistency-checker

class TrieNode{
    val children : MutableMap<Char, TrieNode> = mutableMapOf()
}

class Trie{
    private val root : TrieNode = TrieNode()

    fun insert(word:String){
        var current = root
        for (char in word){
            current = current.children.getOrPut(char) {TrieNode()}
        }
    }

    fun search(word:String): Boolean{
        var current = root
        for (char in word){
            if (char !in current.children){
                return false
            }
            current = current.children[char]!!

        }
        return true
    }
}


fun main() {
    val t = readln().toInt()

    for (i in 1..t) {
        val n = readln().toInt()
        val trie = Trie()
        val elements = (1..n).map { readln() }.sortedDescending()
        var valid = true
        for (e in elements) {
            if (trie.search(e)) {
                println("Case $i: NO")
                valid = false
                break
            }
            trie.insert(e)
        }

        if (valid) {
            println("Case $i: YES")
        }
    }
}
