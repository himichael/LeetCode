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
			
			
			
			
			
			
			
	# 精简代码
    def minimumLengthEncoding(self, words):
        if not words:
            return 0
        root = {}
        self.res = 0
        def insert(word):
            node = root
            for c in word:
                node = node.setdefault(c,{})
        def iteratorTree(node,index):
            if not node:
                self.res += index +1
                return
            for n in node.values():
                iteratorTree(n,index+1)
        for word in words:
            insert(word[::-1])
        for node in root.values():
            iteratorTree(node,1)
        return self.res
			
			
			
	# 利用哈希实现		
	def minimumLengthEncoding(self, words):
		if not words:
			return 0
		good = set(words)
		for word in words:
			for k in xrange(1,len(word)):
				good.discard(word[k:])
		return sum(len(word)+1 for word in good)
		
		
			