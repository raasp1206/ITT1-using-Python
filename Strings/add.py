class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class WordDictionary(object):

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        return self._dfs(0, self.root, word)

    def _dfs(self, index, node, word):
        if index == len(word):
            return node.is_end_of_word
            
        char = word[index]
        
        if char == '.':
            for child in node.children.values():
                if self._dfs(index + 1, child, word):
                    return True
            return False
        
        else:
            if char not in node.children:
                return False
            return self._dfs(index + 1, node.children[char], word)
