class TrieTree(object):
    def __init__(self):
        self.root = {}
        self.end_word = "#"
    
    def insert(self,word,value):
        node = self.root
        for c in word:
            node = node.setdefault(c,{})
        node[self.end_word] = value
        return None

    def find(self,prefix):
        node = self.root
        for c in prefix:
            if(c not in node):
                return None
            node = node[c]
        return node


class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = TrieTree()
        

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: None
        """
        return self.trie.insert(key, val)
        

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        node = self.trie.find(prefix)
        self.count = 0
        
        def recursion(node):
            if(not node):
                return
            for d in node:
                if(d==self.trie.end_word):
                    continue
                if(self.trie.end_word in node[d]):
                    self.count += node[d][self.trie.end_word]
                recursion(node[d])
        if(node):
            recursion(node)
            if(self.trie.end_word in node):
                self.count += node[self.trie.end_word]
        return self.count



# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)