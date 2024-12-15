# Problem: Ada and Indexing
# Solution by Kenny Jesús Flores Huamán
# url: https://www.spoj.com/problems/ADAINDEX/

import sys
input = sys.stdin.readline

class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.prefix_count = 0

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def add(self, s: str) -> None:
        node = self.root
        for c in s:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
            node.prefix_count += 1

    def search(self, s: str) -> int:
        node = self.root
        for c in s:
            if c not in node.children:
                return 0
            node = node.children[c]
        return node.prefix_count

if __name__ == "__main__":
    output = []

    n, q = map(int, input().split())
    trie = Trie()

    for _ in range(n):
        trie.add(input().strip())

    for _ in range(q):
        output.append(str(trie.search(input().strip())))

    sys.stdout.write("\n".join(output) + "\n")