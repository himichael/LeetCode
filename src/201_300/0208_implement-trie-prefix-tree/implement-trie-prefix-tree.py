class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        self.is_end = "#"

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        node = self.root
        for c in word:
            node = node.setdefault(c,{})
        node[self.is_end] = self.is_end

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for c in word:
            if(not node.has_key(c)):
                return False
            node = node[c]
        return node.has_key(self.is_end) 

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for c in prefix:
            if(not node.has_key(c)):
                return False
            node = node[c]
        return True
                

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)  