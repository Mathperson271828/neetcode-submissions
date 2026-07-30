class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            i = ord(char) - ord("a")
            if (node.children[i] == None):
                node.children[i] = TrieNode()
            node = node.children[i]
        node.endOfWord = True

    def search(self, word: str) -> bool:
        node = [self.root]
        for char in word:
            i = ord(char) - ord("a")
            if (char != '.'): 
                new_node = []
                for thing in node:
                    if (thing.children[i]):
                        new_node.append(thing.children[i])
                node = new_node
                if (not node):
                    return False
            else:
                for thing in node:
                    new_node = []
                    for i in range(26):
                        if thing.children[i]:
                            new_node.append(thing.children[i])
                    node = new_node
    
        for thing in node:
            if (thing.endOfWord == True):
                return True
        return False
