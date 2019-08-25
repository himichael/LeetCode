class Trie(object):
    def __init__(self):
        self.root = {}
        
    def insert(self,word):
        node = self.root
        for c in word:
            node = node.setdefault(c,{})
    
class Solution(object):
    def minimumLengthEncoding(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        if(not words):
            return 1
        self.trie = Trie()
        for word in words:
            self.trie.insert(word[::-1])
        
        total = 0
        node = self.trie.root
        self.res = set()
        for c in node.keys():
            if(node[c] == {}):
                self.res.add(c)
                continue
            self.iter(node[c],c)
        for word in self.res:
            total += len(word)
            total += 1
        return total
    
    def iter(self,node,cur_word):
        for c in node:
            if(node[c] == {}):
                self.res.add(cur_word+c)
                continue
            self.iter(node[c],cur_word+c)