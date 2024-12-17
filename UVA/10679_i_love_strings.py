
class Trie:

    def __init__(self):
        self.root = {}

    def add(self, s):
        node = self.root
        for c in s:
            if c not in node:
                node[c] = {}
            node = node[c]

    def search(self, s):
        node = self.root
        for c in s:
            if c not in node:
                return False
            node = node[c]
        return True


k = int(input())

for _ in range(k):
    s = input()
    
    trie = Trie()
    for i in range(0, len(s), 1000):
        trie.add(s[i:i+2000])

    n = int(input())
    for _ in range(n):
        t = input()
        if trie.search(t):
            print("y")
        else:
            print("n")
