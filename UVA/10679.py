import sys
input = sys.stdin.readline

class Trie:
    def __init__(self) -> None:
        self.root = {}

    def add(self, s: str) -> None:
        node = self.root
        for c in s:
            if c not in node:
                node[c] = {}
            node = node[c]

    def isprefix(self, s: str) -> bool:
        node = self.root
        for c in s:
            if c not in node:
                return False
            node = node[c]
        return True

if __name__ == "__main__":
    k = int(input()) 
    for _ in range(k):
        s = input().strip()
        trie = Trie()
        trie.add(s)

        q = int(input())
        for _ in range(q):
            query = input().strip()
            if trie.isprefix(query):
                print("y")
            else:
                print("n")