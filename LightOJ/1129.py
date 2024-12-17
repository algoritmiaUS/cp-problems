# Problem: Consistency Checker
# Solution by Kenny Jesús Flores Huamán
# url: https://lightoj.com/problem/consistency-checker
import sys
input = sys.stdin.readline

class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.end_of_word = False

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    # def add(self, s: str) -> None:
    #     node = self.root
    #     for c in s:
    #         if node.end_of_word:
    #             return False
    #         if c not in node.children:
    #             node.children[c] = TrieNode()
    #         node = node.children[c]
    #         node.end_of_word = True

if __name__ == "__main__":
    output = []
    t = int(input())
    for _ in range(t):
        n = int(input())
        trie = Trie()


    sys.stdout.write("\n".join(output) + "\n")