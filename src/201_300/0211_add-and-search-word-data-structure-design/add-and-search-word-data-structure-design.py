class WordDictionary(object):
    def __init__(self):
        self.root = {}

    def addWord(self, word):
        node = self.root
        for w in word:
            node = node.setdefault(w,{})
        node["#"] = {}      

    def search(self, word):
        node = self.root
        def dfs(word,node):
            if(not word):
                if("#" in node):
                    return True
                return False
            if(word[0]=="."):
                for n in node:
                    if dfs(word[1:],node[n]):
                        return True
            elif(word[0] in node):
                if dfs(word[1:],node[word[0]]):
                    return True
            return False
        return dfs(word,node)